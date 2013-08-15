from gameobject import GameObject

class GameMovable(GameObject):
    def __init__(self, x, y, dx, dy):
        GameObject.__init__(self, x, y)
        self._dx = dx
        self._dy = dy

    def move(self):
        self._x += self._dx
        self._y += self._dx
