
from   game.node import Node
import unittest

class NodeTests(unittest.TestCase):
    def test_node_init_no_params(self):
        n = Node()
        self.assertEqual(n.getName(), 0)
        self.assertEqual(n.getSize(), 2)
        self.assertEqual(n.getX(), 0)
        self.assertEqual(n.getY(), 0)
        self.assertEqual(n.getEdges(), [])

    def test_node_eq(self):
        n1 = Node()
        n2 = Node()
        self.assertEqual(n1, n2)

        n3 = Node(2, 4, 22, 44, [2, 5])
        n4 = Node(2, 4, 22, 44, [2, 5])
        n5 = Node(2, 4, 33, 44, [2, 5])
        self.assertEqual(n3, n4)
        self.assertNotEqual(n3, n5)
        self.assertNotEqual(n1, n3)
        
    def test_node_init_with_params(self):
        n = Node(5, 8, 132, 89, [3, 8, 9])
        self.assertEqual(n.getName(), 5)
        self.assertEqual(n.getSize(), 8)
        self.assertEqual(n.getX(), 132)
        self.assertEqual(n.getY(), 89)
        self.assertSequenceEqual(n.getEdges(), [3, 8, 9])

        n1 = Node(5, 8, 132, 89, [3, 8, 9])
        n2 = Node()
        self.assertEqual(n, n1)
        self.assertEqual([n], [n1])
        self.assertNotEqual(n, n2)

if __name__ == '__main__':
    unittest.main()
