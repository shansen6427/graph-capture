import unittest
from mock import Mock
from game.troopmodel import TroopModel
from game.ui.troopview import TroopView

class TroopModelTests(unittest.TestCase):
    # bind tests
    def testTroopModelBindToViewCallsTroopViewMethodBindToModel(self):
        unit = TroopModelBuilder().build()
        troop_view = Mock(name = 'mock_TroopView')
        troop_view.bindToModel = Mock(name = 'mock_bindToModel')
        unit.bindToView(troop_view)

        self.assertTrue(troop_view.bindToModel.called)

class TroopModelBuilder(object):
    def __init__(self):
        self._id = -1
        self._x = 0
        self._y = 0
        self._dx = 0
        self._dy = 0

    def build(self):
        return TroopModel(self._id, self._x, self._y, self._dx, self._dy)

    def id(self, new_id):
        self._id = new_id
        return self

    def location(self, new_x, new_y):
        self._x = new_x
        self._y = new_y
        return self

    def direction(self, new_dx, new_dy):
        self._dx = new_dx
        self._dy = new_dy
        return self

if __name__ == '__main__':
    unittest.main()