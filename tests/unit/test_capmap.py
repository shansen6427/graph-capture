
from   game.capmap import Capmap
from   game.node import Node
import unittest

class CapmapTests(unittest.TestCase):
    def testCapmapInitializesWithEmptyNodeList(self):
        m = CapmapBuilder().build()
        self.assertEqual(m.getNodes(), [])

    def testGetNodesReturnCorrectNodes(self):
        m = CapmapBuilder().build()
        test_node1 = Node(8, 15, 500, 125, [3, 4])
        test_node2 = Node(3, 2, 300, 185, [])
        test_node3 = Node(50, 70, 250, 300, [5, 7, 6])
        test_nodes = [test_node1, test_node2, test_node3]
        m._nodes = test_nodes

        self.assertSequenceEqual(m.getNodes(), test_nodes)
    
    def testTheDefaultMapStartsWithExactlyTheseNodes(self):
        m = CapmapBuilder().build()
        m.useDefaultMap()
        default_node1 = Node(0, 20, 100, 100, [1])
        default_node2 = Node(1, 20, 300, 300, [0])
        default_nodes = [default_node1, default_node2]
        
        self.assertSequenceEqual(m.getNodes(), default_nodes)

class CapmapBuilder():
    def __init__(self):
        self._map = Capmap()

    def build(self):
        return self._map

if __name__ == '__main__':
    unittest.main()
