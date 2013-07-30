from   game.capmap import Capmap
import unittest

class CapmapTests(unittest.TestCase):
    def test_map_init(self):
        m = Capmap()
        self.assertEqual(m.nodes, [])

    
    def testTheDefaultMapStartsWithExactlyTheseNodes(self):
        m = Capmap()
        m.default_map()
        n1 = Node(0, 5, 100, 100, [1])
        n2 = Node(1, 5, 200, 200, [0])
        self.assertSequenceEqual(m.nodes, [n1, n2])

if __name__ == '__main__':
    unittest.main()
