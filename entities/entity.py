from abc import ABC, abstractmethod

from utils import Color
from utils import Direction
from utils import PacmanConstants

class Entity(ABC):

    def __init__(self, x: float = 0.0, y: float = 0.0, color: Color = Color.BLACK):
        self._x = x
        self._y = y
        self._direction: Direction = Direction.NONE
        self._color = color
        self._mode: float = 0.8

    def update(self, dt):
        return self.next_cell()

    @abstractmethod
    def move(self, dt):
        pass
    
    @abstractmethod
    def next_cell(self):
        pass

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

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    def get_speed(self):
        return PacmanConstants.BASE_SPEED * self._mode

