# troop tests

from game.troop import Troop
import unittest
import pygame
from mock import Mock

class TroopTests(unittest.TestCase):

    # initialization tests
    def testTroopInitializedWithNoParametersHasCorrectValues(self):
        unit = Troop()

        self.assertEqual(unit.getId(), -1)
        self.assertEqual(unit.image, None)
        self.assertEqual(unit.rect, None)

    def testTroopInitializedWithCertainParametersHasCorrectValues(self):
        unit = Troop(5)

        self.assertEqual(unit.getId(), 5)
        self.assertEqual(unit.getImage(), None)
        self.assertEqual(unit.getRect(), None)

    def testTroopInitializationCallsSpriteInit(self):
        pygame.sprite.Sprite.__init__ = Mock()
        unit = Troop()

        pygame.sprite.Sprite.__init__.assert_called_once_with(unit)

    # selector tests
    def testTroopGetIdWithUnassignedIdReturnsCorrectId(self):
        unit = Troop()

        self.assertEqual(unit.getId(), -1)

    def testTroopGetIdWithManuallyAssignedIdReturnsCorrectId(self):
        unit = Troop()
        unit._id = 83

        self.assertEqual(unit.getId(), 83)

    def testTroopGetImageForTroopWithANoneImageReturnsCorrectImage(self):
        unit = Troop()

        self.assertEqual(unit.getImage(), None)

    def testTroopGetImageForManuallyAssignedImageReturnsCorrectImage(self):
        unit = Troop()
        image = pygame.Surface((10,10))
        unit.image = image

        self.assertEqual(unit.getImage(), unit.image)

    def testTroopGetRectForTroopWithANoneRectReturnsCorrectRect(self):
        unit = Troop()

        self.assertEqual(unit.getRect(), None)

    def testTroopGetRectForManuallyAssignedRectReturnsCorrectRect(self):
        unit = Troop()
        surface = pygame.Surface((10,10))
        rect = surface.get_rect()
        unit.rect = rect

        self.assertEqual(unit.getRect(), unit.rect)

    # image tests
    def testTroopCreateImageAssignsASurfaceToTroopImageAttribute(self):
        unit = Troop()
        unit.createImage()

        self.assertIs(type(unit.getImage()), pygame.Surface)

    def testTroopCreateImageAssignsARectToTroopRectAttribute(self):
        unit = Troop()
        unit.createImage()

        self.assertIs(type(unit.getRect()), pygame.Rect)

    def testTroopRectAttributeHasCorrectDimensionsAfterCreateImageCall(self):
        unit = Troop()
        unit.createImage()
        unit_rect = unit.getRect()
        correct_width = 10
        correct_height = 10

        self.assertEqual(unit_rect.width, correct_width)
        self.assertEqual(unit_rect.height, correct_height)

    def testTroopColorSpriteMethodCallsSurfaceFillMethod(self):
        unit = Troop()
        unit.createImage()
        unit.image = Mock()
        unit.colorSprite((0,0,0))

        unit.image.fill.assert_called_once_with((0,0,0))

if __name__ == '__main__':
    unittest.main()