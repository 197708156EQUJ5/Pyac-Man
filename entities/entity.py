from utils import Color
from utils import Direction

class Entity():

    def __init__(self, x: float = 0.0, y: float = 0.0, color: Color = Color.BLACK):
        self._x = x
        self._y = y
        self._direction: Direction = Direction.LEFT
        self._color = color

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
