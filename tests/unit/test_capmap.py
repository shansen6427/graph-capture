
from   game.capmap import Capmap
from   game.node import Node
import unittest

class CapmapTests(unittest.TestCase):
    def test_map_init(self):
        m = Capmap()
        self.assertEqual(m.getNodes(), [])
    
    def testTheDefaultMapStartsWithExactlyTheseNodes(self):
        m = Capmap()
        m.useDefaultMap()
        n1 = Node(0, 20, 100, 100, [1])
        n2 = Node(1, 20, 300, 300, [0])
        self.assertSequenceEqual(m.getNodes(), [n1, n2])

if __name__ == '__main__':
    unittest.main()
