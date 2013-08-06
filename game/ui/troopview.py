import pygame

class TroopView(pygame.sprite.Sprite):
    def __init__(self, pygame_module):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self._pygame_module = pygame_module

    def createImage(self):
        self.image = self._pygame_module.Surface((10,10))
        self.rect = self.image.get_rect()

    def colorSprite(self, rgb):
        self.image.fill(rgb)

    @property
    def pygame_module(self):
        return self._pygame_module