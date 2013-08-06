import unittest
from game.troopmodel import TroopModel
from game.ui.troopview import TroopView
from tests.unit.test_troopmodel import TroopModelBuilder
from tests.unit.test_troopview import TroopViewBuilder

class TroopModelAndViewTests(unittest.TestCase):
    # binding tests
    def testTroopViewHasSameLocationAsTroopModelAfterBinding(self):
        unit_model = TroopModelBuilder().location(40, 60).build()
        unit_view = TroopViewBuilder().build()

        unit_model.bindToView(unit_view)

        self.assertEqual(unit_model.location, unit_view.location_binding())

if __name__ == '__main__':
    unittest.main()
