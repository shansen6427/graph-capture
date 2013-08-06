import unittest
from mock import Mock
import pygame
from game.ui.troopview import TroopView

class TroopViewTests(unittest.TestCase):
    # initialization tests
    def testTroopViewInitializationWithCertainParametersHasCorrectAttributeValues(self):
        unit = TroopViewBuilder().pygameModule(pygame).build()

        self.assertEqual(unit.pygame_module, pygame)
        self.assertEqual(unit.image, None)
        self.assertEqual(unit.rect, None)

    def testTroopViewCreateImageAssignsASurfaceToTroopImageAttribute(self):
        unit = TroopViewBuilder().pygameModule(pygame).build()
        unit.createImage()

        self.assertIs(type(unit.image), pygame.Surface)

    def testTroopViewCreateImageAssignsARectToTroopRectAttribute(self):
        rect = object()
        surface = Mock(name='mock_surface')
        surface.get_rect.return_value = rect
        pygame_module = _createPygameWithSurface(surface)

        unit = TroopViewBuilder().pygameModule(pygame_module).build()
        unit.createImage()
        pygame_module.Surface.assert_called_once_with((10,10))

        self.assertEquals(unit.rect, rect)

    def testTroopViewColorSpriteMethodCallsSurfaceFillMethod(self):
        rgb = object()
        surface = Mock(name='mock_surface')
        pygame_module = _createPygameWithSurface(surface)

        unit = TroopViewBuilder().pygameModule(pygame_module).build()
        unit.createImage()
        unit.colorSprite(rgb)

        surface.fill.assert_called_once_with(rgb)

def _createPygameWithSurface(surface):
    pygame = Mock(name='mock_pygame')
    pygame.Surface.return_value = surface
    return pygame

class TroopViewBuilder(object):
    def __init__(self):
        self._pygame_module = None

    def build(self):
        return TroopView(self._pygame_module)

    def pygameModule(self, new_pygame_module):
        self._pygame_module = new_pygame_module
        return self

if __name__ == '__main__':
    unittest.main()