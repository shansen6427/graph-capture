import unittest
from game.gamemovable import GameMovable


class GameMovableTests(unittest.testsuite):
    def testMovableMoveMethodUpdatesLocationCorrectly(self):
        unit = GameMovable(0, 0, 25, 50)
        unit.move()

        self.assertEqual(unit.x, 25)
        self.assertEqual(unit.y, 50)

        unit.move()

        self.assertEqual(unit.x, 50)
        self.assertEqual(unit.y, 100)