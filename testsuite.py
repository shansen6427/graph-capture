# testsuite.py

import unittest
from capmap import Capmap
from node import Node
from game import Game_Node

class TestSuite(unittest.TestCase):

    # node tests
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

        
    # map tests
    def test_map_init(self):
        m = Capmap()
        self.assertEqual(m.nodes, [])

    
    def test_default_map(self):
        m = Capmap()
        m.default_map()
        n1 = Node(0, 5, 100, 100, [1])
        n2 = Node(1, 5, 200, 200, [0])
        self.assertSequenceEqual(m.nodes, [n1, n2])

    # game tests
    def test_game_node_init_no_params(self):
        n0 = Node()
        n = Game_Node(n0)
        self.assertEqual(n.name, 0)
        self.assertEqual(n.size, 2)
        self.assertEqual(n.x, 0)
        self.assertEqual(n.y, 0)
        self.assertEqual(n.edges, [])
        self.assertEqual(n.surface, None)

    def test_game_node_eq(self):
        n01 = Node()
        n02 = Node()
        n1 = Game_Node(n01)
        n2 = Game_Node(n02)
        self.assertEqual(n1, n2)

        n03 = Node(2, 4, 22, 44, [2, 5])
        n04 = Node(2, 4, 22, 44, [2, 5])
        n05 = Node(2, 4, 33, 44, [2, 5])
        n3 = Game_Node(n03)
        n4 = Game_Node(n04)
        n5 = Game_Node(n05)
        self.assertEqual(n3, n4)
        self.assertNotEqual(n3, n5)
        self.assertNotEqual(n1, n3)
        
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

if __name__ == '__main__':
    unittest.main()
