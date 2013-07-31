
from   game.node import Node
import unittest

class NodeTests(unittest.TestCase):
    """
    empty node properties:
        name: 0
        size: 0
        x: 0
        y: 0
        edges: []
    """

    # get method tests
    def testNodeGetNameReturnsCorrectName(self):
        unit = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertEquals(unit.getName(), 5)

    def testNodeGetSizeReturnsCorrectSize(self):
        unit = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertEquals(unit.getSize(), 25)

    def testNodeGetXReturnsCorrectXPosition(self):
        unit = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertEquals(unit.getX(), 125)

    def testNodeGetYReturnsCorrectYPosition(self):
        unit = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertEquals(unit.getY(), 255)

    def testNodeGetEdgesReturnsCorrectEdgeList(self):
        unit = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertSequenceEqual(unit.getEdges(), [9, 4, 2])

    # node initialization tests
    def testNodeInitializedWithNoParametersHasCorrectValues(self):
        unit = Node()

        self.assertEqual(unit.getName(), 0)
        self.assertEqual(unit.getSize(), 0)
        self.assertEqual(unit.getX(), 0)
        self.assertEqual(unit.getY(), 0)
        self.assertEqual(unit.getEdges(), [])

    def testNodeInitializedWithCertainParametersHasCorrectValues(self):
        n = Node(5, 8, 132, 89, [3, 8, 9])
        
        self.assertEqual(n.getName(), 5)
        self.assertEqual(n.getSize(), 8)
        self.assertEqual(n.getX(), 132)
        self.assertEqual(n.getY(), 89)
        self.assertSequenceEqual(n.getEdges(), [3, 8, 9])

    # __eq__ method tests
    def testNodeEqMethodReturnsTrueWhenComparingEmptyNodes(self):
        unit1 = Node()
        unit2 = Node()
        
        self.assertEqual(unit1, unit2)

    def testNodeEqMethodReturnsTrueWhenComparingIdenticalNodes(self):
        unit1 = Node(5, 25, 125, 255, [9, 4, 2])
        unit2 = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertEqual(unit1, unit2)
        
    def testNodeEqMethodReturnsFalseWhenComparingEmptyAndDefinedNodes(self):
        unit1 = Node()
        unit2 = Node(5, 25, 125, 255, [9, 4, 2])
        
        self.assertNotEqual(unit1, unit2)

    def testNodeEqMethodReturnsFalseWhenComparingNodesWithDifferentValues(self):
        unit1 = Node(5, 25, 125, 255, [9, 4, 2])
        unit2 = Node(2, 90, 45, 46, [])

        self.assertNotEqual(unit1, unit2)
        

class NodeBuilder():
    def __init__(self):
        self._node = Node()
    
    def build(self):
        return Node()

    def setNode(self, node):
        self._node = node
        return self
    
if __name__ == '__main__':
    unittest.main()
