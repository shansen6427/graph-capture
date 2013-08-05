import unittest
from game.troopmodel import TroopModel

class TroopModelTests(unittest.TestCase):
     # initialization tests
    def testTroopInitializedWithCertainParametersHasCorrectAttributeValues(self):
        unit = TroopModelBuilder().setNextId(0).x(50).y(95).direction((3,1)).build()

        self.assertEqual(unit.id, 0)
        self.assertEqual(unit.x, 50)
        self.assertEqual(unit.y, 95)
        self.assertEqual(unit.direction, (3,1))

    def testFirstFourTroopModelsInstantiatedHaveCorrectIds(self):
        TroopModelBuilder().setNextId(0)

        # units should have id's equal to their creation order, starting with 0
        for x in xrange(4):
            unit = TroopModelBuilder().build()
            self.assertEqual(unit.id, x)

    # move tests
    def testTroopModelMoveUpdatesLocationCorrectly(self):
        unit = TroopModelBuilder().x(0).y(0).direction((6,8)).build()

        self.assertEqual((unit.x, unit.y), (0, 0))

        unit.move()

        self.assertEqual((unit.x, unit.y), (6,8))

        unit.move()

        self.assertEqual((unit.x, unit.y), (12, 16))

    # miscellaneous tests
    def testTroopModelIdCannotGoAboveMaxIdValue(self):
        unit = TroopModelBuilder().setNextId(TroopModel._max_id).build()

        self.assertEqual(unit.id, TroopModel._max_id)

        unit = TroopModelBuilder().build()

        self.assertEqual(unit.id, 0)


class TroopModelBuilder(object):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._direction = None

    def build(self):
        return TroopModel(self._x, self._y, self._direction)

    def setNextId(self, new_next_id):
        TroopModel._next_id = new_next_id
        return self

    def x(self, new_x):
        self._x = new_x
        return self

    def y(self, new_y):
        self._y = new_y
        return self

    def direction(self, new_direction):
        self._direction = new_direction
        return self

if __name__ == '__main__':
    unittest.main()