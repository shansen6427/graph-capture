import pygame

class Troop(pygame.sprite.Sprite):
    def __init__(self, pygameModule, id = -1):
        self._pygame = pygameModule
        self._pygame.sprite.Sprite.__init__(self)
        self._id = id
        self.image = None #<--- these look private; rename to _image and _rect
        self.rect = None

    # sprite methods
    def createImage(self):
        self.image = self._pygame.Surface((10,10)) #<--- if this is a surface, why is it called "image"? call it _surface, keep things simple
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
