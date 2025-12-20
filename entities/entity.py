from utils import Color
from utils import Direction

class Entity():

    def __init__(self, x: float = 0.0, y: float = 0.0, color: Color = Color.BLACK):
        self._x = x
        self._y = y
        self._direction: Direction = Direction.LEFT
        self._color = color

    def move(self) -> bool:
        if self._direction == Direction.LEFT:
            self._x -= 0.1
        elif self._direction == Direction.RIGHT:
            self._x += 0.1
        elif self._direction == Direction.UP:
            self._y -= 0.1
        elif self._direction == Direction.DOWN:
            self._y += 0.1
        return False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def color(self):
        return self._color
