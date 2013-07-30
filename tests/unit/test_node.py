from   game.node import Node
import unittest

class NodeTests(unittest.TestCase):
    def test_node_init_no_params(self):
        n = Node()
        self.assertEqual(n.name, 0)
        self.assertEqual(n.size, 2)
        self.assertEqual(n.x, 0)
        self.assertEqual(n.y, 0)
        self.assertEqual(n.edges, [])

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
        self.assertEqual(n.name, 5)
        self.assertEqual(n.size, 8)
        self.assertEqual(n.x, 132)
        self.assertEqual(n.y, 89)
        self.assertSequenceEqual(n.edges, [3, 8, 9])

        n1 = Node(5, 8, 132, 89, [3, 8, 9])
        n2 = Node()
        self.assertEqual(n, n1)
        self.assertEqual([n], [n1])
        self.assertNotEqual(n, n2)

if __name__ == '__main__':
    unittest.main()