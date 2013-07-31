
from   game.node import Node
from   game.game import GameNode
import unittest

class GameNodeTests(unittest.TestCase):
    def testCanConstructADefaultGameNodeAndItHasCertainProperties(self):
        unit = GameNodeBuilder().build()

        self.assertEqual(unit.getName(), 0)
        self.assertEqual(unit.getSize(), 0)
        self.assertEqual(unit.getX(), 0)
        self.assertEqual(unit.getY(), 0)
        self.assertEqual(unit.getEdges(), [])
        self.assertEqual(unit.getSurface(), None)

    def testGameNodeInitializedWithCertainParamatersHasCorrectValues(self):
        test_node = Node(5, 8, 132, 89, [3, 8, 9])
        unit = GameNodeBuilder().setNode(test_node).build()
        
        self.assertEqual(unit.getName(), 5)
        self.assertEqual(unit.getSize(), 8)
        self.assertEqual(unit.getX(), 132)
        self.assertEqual(unit.getY(), 89)
        self.assertSequenceEqual(unit.getEdges(), [3, 8, 9])
        self.assertEqual(unit.getSurface(), None)

    def testEmptyGameNodesAreEqual(self):
        unit1 = GameNodeBuilder()
        unit2 = GameNodeBuilder()
        
        self.assertEqual(unit1._node, unit2._node)

    def testGameNodesWithTheSameNodeAreEqual(self):
        node1 = Node(2, 4, 22, 44, [2, 5])
        node2 = Node(2, 4, 22, 44, [2, 5])
        unit1 = GameNodeBuilder().setNode(node1).build()
        unit2 = GameNodeBuilder().setNode(node2).build()
        
        self.assertEqual(unit1, unit2)
       
    def testGameNodesWithDifferentNodesAreNotEqual(self): 
        node1 = Node(2, 4, 22, 44, [2, 5])
        node2 = Node(2, 4, 33, 44, [2, 5])
        unit1 = GameNodeBuilder().setNode(node1).build()
        unit2 = GameNodeBuilder().setNode(node2).build()
        
        self.assertNotEqual(unit1, unit2)


class GameNodeBuilder():
    def __init__(self):
        self._node = Node()

    def build(self):
        return GameNode(self._node)

    def setNode(self, newNode):
        self._node = newNode
        return self


if __name__ == '__main__':
    unittest.main()
