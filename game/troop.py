"""
    troop.py
    Troop class.  This class represents armies travelling between nodes; they
    can capture other nodes, reinforce friendly nodes and destroy other troops.
"""
import pygame

class Troop(pygame.sprite.Sprite):
    def __init__(self, id = -1):
        pygame.sprite.Sprite.__init__(self)
        self._id = id
        self.image = None
        self.rect = None

    # sprite methods
    def createImage(self):
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()

    def colorSprite(self, rgb):
        self.image.fill(rgb)

    # selector methods
    def getId(self):
        return self._id

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect