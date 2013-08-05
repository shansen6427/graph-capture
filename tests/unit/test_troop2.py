#!/usr/bin/python

from   game.troop2 import Troop
from   mock import Mock, patch
import pygame
import unittest

class TroopTests(unittest.TestCase):

    # initialization tests
    def testTroopInitializedWithNoParametersHasCorrectValues(self):
        unit = TroopBuilder().build()

        self.assertEqual(unit.getId(), -1)
        self.assertEqual(unit.image, None)
        self.assertEqual(unit.rect, None)

    def testTroopInitializedWithCertainParametersHasCorrectValues(self):
        unit = TroopBuilder().id(5).build()

        self.assertEqual(unit.getId(), 5)
        self.assertEqual(unit.getImage(), None)
        self.assertEqual(unit.getRect(), None)

    def testTroopInitializationCallsSpriteInit(self):
        init = Mock(name='init')
        class MockSprite(object): pass
        MockSprite.__init__ = init #<--- mock can't mock __init__, so we have to get around it this way
        spriteModule = Mock(name='spriteModule')
        spriteModule.Sprite = MockSprite
        pygameModule = Mock(name='pygameModule')
        pygameModule.sprite = spriteModule

        unit = TroopBuilder().pygame(pygameModule).build()

        # self.assertEquals(self._savedSpriteSelf, unit) 
        init.assert_called_once_with(unit)

    # selector tests
    def testTroopGetIdWithUnassignedIdReturnsCorrectId(self): #<--- you already test this in testTroopInitializedWithNoParametersHasCorrectValues
        unit = TroopBuilder().build()

        self.assertEqual(unit.getId(), -1)

    def testTroopGetIdWithManuallyAssignedIdReturnsCorrectId(self): #<--- why would you directly assign to a private variable? don't test this, it's an implementation detail
        unit = TroopBuilder().build()
        unit._id = 83

        self.assertEqual(unit.getId(), 83)

    def testTroopGetImageForTroopWithANoneImageReturnsCorrectImage(self): #<--- you already test this in testTroopInitializedWithNoParametersHasCorrectValues
        unit = TroopBuilder().build()

        self.assertEqual(unit.getImage(), None)

    def testTroopGetImageForManuallyAssignedImageReturnsCorrectImage(self): #<--- better named "testCanSetAndGetImage"; that's what you're doing, right?
        unit = TroopBuilder().build()
        #image = pygame.Surface((10,10)) # <--- no need to make this _actually_ a surface; your code doesn't care, so why should your test? pass in any old object
        image = object()
        unit.image = image

        self.assertEqual(unit.getImage(), unit.image)

    def testTroopGetRectForTroopWithANoneRectReturnsCorrectRect(self): #<--- already tested in testTroopInitializedWithNoParametersHasCorrectValues
        unit = TroopBuilder().build()

        self.assertEqual(unit.getRect(), None)

    def testTroopGetRectForManuallyAssignedRectReturnsCorrectRect(self): #<--- better named "testCanSetAndGetRect"
        unit = TroopBuilder().build()
        #surface = pygame.Surface((10,10))
        #rect = surface.get_rect() # <--- same thing; use the simplest test possible. this points out what your code _really_ does, not what you imagine it does
        rect = object()
        unit.rect = rect

        self.assertEqual(unit.getRect(), unit.rect)

    # image tests
    def testTroopCreateImageAssignsASurfaceToTroopImageAttribute(self):
        unit = TroopBuilder().pygame(pygame).build()
        unit.createImage()

        self.assertIs(type(unit.getImage()), pygame.Surface)

    def testTroopCreateImageAssignsARectToTroopRectAttribute(self):
        rect = object()
        surface = Mock(name='surface')
        surface.get_rect.return_value = rect
        pygameModule = Mock(name='pygame') # <--- always give mocks a name so you can identify what mock you're actually using during a test 
        pygameModule.Surface.return_value = surface
        
        unit = TroopBuilder().pygame(pygameModule).build()
        unit.createImage()
        pygameModule.Surface.assert_called_once_with((10,10)) #<--- our code doesn't actually care (yet) about the properties the resulting rect has; it just cares that we invoked the Surface method correctly, so that's what we'll test for here

        actualRect = unit.getRect()
        self.assertEquals(actualRect, rect) #<--- because we mocked, we have greater control, so can assert for actual equality here, not just a type

    def testTroopRectAttributeHasCorrectDimensionsAfterCreateImageCall(self): # <-- moved into above test
        pass

    def testTroopColorSpriteMethodCallsSurfaceFillMethod(self):
        rgb = object()  #<--- generic object; nothing in your code required rgb be a tuple
        surface = Mock(name='surface')
        pygame = _createPygameWithSurface(surface) #<--- at this point, i notice i have to keep creating the same pygame as the other tests, with all the same mock plumbing. so i make a helper method 

        unit = TroopBuilder().pygame(pygame).build()
        unit.createImage()
        unit.colorSprite(rgb)

        # unit.image.fill.assert_called_once_with((0,0,0)) #<--- shouldn't have to inspect into the image; if you inject your surface, then it's already exposed. cleaner, easier to read, and doesn't get caught up in internal workings of class
        surface.fill.assert_called_once_with(rgb)

def _createPygameWithSurface(surface):
    pygame = Mock(name='helper._pygame')
    pygame.Surface.return_value = surface
    return pygame

class TroopBuilder(object):
    def __init__(self):
        self._id = None
        self._pygame = Mock(name='builder._pygame') #<--- unique name here, so i can tell "oh shit, my test isn't working because i forgot to inject my test's custom mock into the builder"

    def build(self):
        if self._id is None:
            return Troop(self._pygame)
        return Troop(self._pygame, self._id)

    def pygame(self, newPygame):
        self._pygame = newPygame
        return self

    def id(self, newId):
        self._id = newId
        return self


if __name__ == '__main__':
    unittest.main()
