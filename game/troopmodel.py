class TroopModel(object):
    _next_id = 0
    _max_id = 999

    def __init__(self, x, y, direction):
        self._id = TroopModel._next_id
        TroopModel._next_id += 1

        self._location = [x, y]
        self._direction = direction

        if TroopModel._next_id > TroopModel._max_id:
            TroopModel._next_id = 0

    def bindToView(self, TroopView):
        TroopView.bindToModel(lambda: self._location)

    def move(self):
        self._location[0] += self._direction[0]
        self._location[1] += self._direction[1]

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    @property
    def direction(self):
        return self._direction