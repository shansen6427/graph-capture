class TroopModel(object):
    _next_id = 0
    _max_id = 999

    def __init__(self, x, y, direction):
        self._id = TroopModel._next_id
        TroopModel._next_id += 1

        self._x = x
        self._y = y
        self._direction = direction

        if TroopModel._next_id > TroopModel._max_id:
            TroopModel._next_id = 0

    def move(self):
        self._x += self._direction[0]
        self._y += self._direction[1]

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def direction(self):
        return self._direction