from   game.game import GraphCapture
from   game.node import Node
from   mock import Mock
import unittest

class GameTests(unittest.TestCase):
    # initialization tests
    def testGraphCaptureInitializesWithCorrectValues(self):
        unit = GraphCaptureBuilder().build()

        self.assertEqual(unit._game_map, None)
        self.assertEqual(unit._game_nodes, [])
        self.assertEqual(unit._num_nodes, 0)

    # createPaths method tests
    def testCreatePathsCallsPygameQuitWhenPassedEmptyList(self):
        pygame = Mock(name='pygame')

        unit = GraphCaptureBuilder().pygame(pygame).build()
        try:
            unit.createPaths([])
        except SystemExit:
            pass

        pygame.quit.assert_called_once_with()

    def testCreatePathsRaisesSystemExitWhenPassedEmptyList(self):
        unit = GraphCaptureBuilder().build()

        self.assertRaises(SystemExit, unit.createPaths, [])
    
    def testCreatePathsReturnsCorrectStartPoints(self):
        node1 = Node(0, 20, 50, 60, [1,2])
        node2 = Node(1, 30, 30, 100, [0])
        node3 = Node(2, 40, 150, 80, [0])
        nodes = [node1, node2, node3]
        correct_start_points = [(60, 70), (60, 70), (45, 115), (170, 100)]

        # create paths
        unit = GraphCaptureBuilder().build()
        paths = unit.createPaths(nodes)

        # gets start points from paths
        path_start_points = [path[0] for path in paths]
    
        self.assertSequenceEqual(path_start_points, correct_start_points)
        
        
    def testCreatePathsReturnsCorrectEndPoints(self):
        node1 = Node(0, 20, 50, 60, [1,2])
        node2 = Node(1, 30, 30, 100, [0])
        node3 = Node(2, 40, 150, 80, [0])
        nodes = [node1, node2, node3]
        correct_end_points = [(45, 115), (170, 100), (60, 70), (60, 70)]

        # create paths
        unit = GraphCaptureBuilder().build()
        paths = unit.createPaths(nodes)

        # gets end points from paths
        path_end_points = [path[1] for path in paths]
    
        self.assertSequenceEqual(path_end_points, correct_end_points)


class GraphCaptureBuilder():
    def __init__(self):
        self._pygame = Mock(name='builder._pygame')
    
    def build(self):
        return GraphCapture(self._pygame)

    def pygame(self, newPygame):
        self._pygame = newPygame
        return self


if __name__ == '__main__':
    unittest.main()
