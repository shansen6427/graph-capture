import unittest
from game.troopmodel import TroopModel
from game.ui.troopview import TroopView
#from tests.unit.test_troopmodel import TroopModelBuilder
from tests.unit.test_troopmodel2 import TroopModelBuilder
from tests.unit.test_troopview2 import TroopViewBuilder

class TroopModelAndViewTests(unittest.TestCase):
    # binding tests
    def testTroopViewHasSameLocationAsTroopModelAfterBinding(self):
        model = TroopModelBuilder().id(0).location(50, 80).direction(100, -30).build()
        view = TroopViewBuilder().build()

        model.bindToView(view)

        self.assertEqual(model.x, view._x_binding())
        self.assertEqual(model.y, view._y_binding())

if __name__ == '__main__':
    unittest.main()
