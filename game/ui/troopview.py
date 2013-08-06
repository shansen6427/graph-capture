import pygame

class TroopView(pygame.sprite.Sprite):
    def __init__(self, pygame_module):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self._pygame_module = pygame_module
        self._location_binding = None

    def bindToModel(self, binding):
        self._location_binding = binding

    def validateBinding(self):
        if self._location_binding == None: raise Exception("TroopView has no location in validateBinding")

    def createImage(self):
        self.image = self._pygame_module.Surface((10,10))
        self.rect = self.image.get_rect()

    def colorSprite(self, rgb):
        self.image.fill(rgb)

    @property
    def pygame_module(self):
        return self._pygame_module

    @property
    def location_binding(self):
        return self._location_binding