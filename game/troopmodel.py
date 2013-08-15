from gamemovable import GameMovable

class TroopModel(GameMovable):
    def __init__(self, new_id, x, y, dx, dy):
        GameMovable.__init__(self, x, y, dx, dy)
        self._id = new_id

    def bindToView(self, TroopView):
        TroopView.bindToModel(lambda: self.x, lambda: self.y)

    @property
    def id(self):
        return self._id