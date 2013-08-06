import unittest
from mock import Mock
from game.troopmodel import TroopModel
from game.ui.troopview import TroopView

class TroopModelTests(unittest.TestCase):
     # initialization tests
    def testTroopInitializedWithCertainParametersHasCorrectAttributeValues(self):
        unit = TroopModelBuilder().setNextId(0).location(50, 95).direction((3,1)).build()

        self.assertEqual(unit.id, 0)
        self.assertEqual(unit.location, [50, 95])
        self.assertEqual(unit.direction, (3,1))

    def testFirstFourTroopModelsInstantiatedHaveCorrectIds(self):
        TroopModelBuilder().setNextId(0)

        # units should have id's equal to their creation order, starting with 0
        for x in xrange(4):
            unit = TroopModelBuilder().build()
            self.assertEqual(unit.id, x)

    # move tests
    def testTroopModelMoveUpdatesLocationCorrectly(self):
        unit = TroopModelBuilder().location(0,0).direction((6,8)).build()

        self.assertEqual(unit.location, [0, 0])

        unit.move()

        self.assertEqual(unit.location, [6,8])

        unit.move()

        self.assertEqual(unit.location, [12, 16])

    # bind tests
    def testTroopModelBindToViewCallsTroopViewMethodBindToModel(self):
        unit = TroopModelBuilder().build()
        troop_view = Mock(name = 'mock_TroopView')
        troop_view.bindToModel = Mock(name = 'mock_bindToModel')
        unit.bindToView(troop_view)

        self.assertTrue(troop_view.bindToModel.called)

    # miscellaneous tests
    def testTroopModelIdCannotGoAboveMaxIdValue(self):
        unit = TroopModelBuilder().setNextId(TroopModel._max_id).build()

        self.assertEqual(unit.id, TroopModel._max_id)

        unit = TroopModelBuilder().build()

        self.assertEqual(unit.id, 0)


class TroopModelBuilder(object):
    def __init__(self):
        self._location = [0, 0]
        self._direction = None

    def build(self):
        return TroopModel(self._location[0], self._location[1], self._direction)

    def setNextId(self, new_next_id):
        TroopModel._next_id = new_next_id
        return self

    def location(self, new_x, new_y):
        self._location = [new_x, new_y]
        return self

    def direction(self, new_direction):
        self._direction = new_direction
        return self

if __name__ == '__main__':
    unittest.main()