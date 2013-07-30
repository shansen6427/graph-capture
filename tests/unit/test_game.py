from   game.node import Node
from   game.game import Game_Node
import unittest

class GameNodeTests(unittest.TestCase):
    def testCanConstructADefaultGameNodeAndItHasCertainProperties(self):
        unit = GameNodeBuilder().build()

        self.assertEqual(unit.name, 0)
        self.assertEqual(unit.size, 2)
        self.assertEqual(unit.x, 0)
        self.assertEqual(unit.y, 0)
        self.assertEqual(unit.edges, [])
        self.assertEqual(unit.surface, None)

    def testEmptyGameNodesAreEqual(self):
        unit1 = GameNodeBuilder()
        unit2 = GameNodeBuilder()
        self.assertEqual(unit1, unit2)

    def testGameNodesWithTheSameNodeAreEqual(self):
        node1 = Node(2, 4, 22, 44, [2, 5])
        node2 = Node(2, 4, 22, 44, [2, 5])
        
        unit1 = GameNodeBuilder().node(node1).build()
        unit2 = GameNodeBuilder().node(node2).build()
        
        self.assertEqual(unit1, unit2)
       
    def testGameNodesWithDifferentNodesAreNotEqual(self): 
        node1 = Node(2, 4, 22, 44, [2, 5])
        node2 = Node(2, 4, 33, 44, [2, 5])
        unit1 = GameNodeBuilder().node(node1).build()
        unit2 = GameNodeBuilder().node(node2).build()
        self.assertNotEqual(unit1, unit2)
        
    def test_node_init_with_params(self):
        n0 = Node(5, 8, 132, 89, [3, 8, 9])
        n = Game_Node(n0)
        self.assertEqual(n.name, 5)
        self.assertEqual(n.size, 8)
        self.assertEqual(n.x, 132)
        self.assertEqual(n.y, 89)
        self.assertSequenceEqual(n.edges, [3, 8, 9])
        self.assertEqual(n.surface, None)

        n01 = Node(5, 8, 132, 89, [3, 8, 9])
        n02 = Node()
        n1 = Game_Node(n01)
        n2 = Game_Node(n02)
        self.assertEqual(n, n1)
        self.assertEqual([n], [n1])
        self.assertNotEqual(n, n2)


class GameNodeBuilder(self):
    def __init__(self):
        self._node = Node()

    def build(self):
        return Game_Node(self._node)

    def node(self, newNode):
        self._node = newNode
        return self


if __name__ == '__main__':
    unittest.main()
