import pygame

class TroopView(pygame.sprite.Sprite):
    def __init__(self, pygame_module):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self._pygame_module = pygame_module
        self._x_binding = None
        self._y_binding = None

    def bindToModel(self, x_binding, y_binding):
        self._x_binding = x_binding
        self._y_binding = y_binding

    def _validateBindings(self):
        if (self._x_binding is None or
                self._y_binding is None): raise Exception("TroopView has no location in validateBinding")

    def createImage(self):
        self.image = self._pygame_module.Surface((10,10))
        self.rect = self.image.get_rect()

    def colorSprite(self, rgb):
        self.image.fill(rgb)