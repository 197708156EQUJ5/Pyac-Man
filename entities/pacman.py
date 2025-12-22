import math

from entities import Entity
from utils import Color
from utils import PacmanConstants
from utils import Direction

class Pacman(Entity):

    def __init__(self):
        super().__init__(PacmanConstants.INIT[0], PacmanConstants.INIT[1], color=Color.YELLOW)
        self._user_direction: Direction = Direction.NONE

    def move(self, dt):
        delta = dt * PacmanConstants.BASE_SPEED * self._mode
        if self._direction == Direction.LEFT:
            self._x -= delta
        elif self._direction == Direction.RIGHT:
            self._x += delta
        elif self._direction == Direction.UP:
            self._y -= delta
        elif self._direction == Direction.DOWN:
            self._y += delta

    def next_cell(self):
        x, y = (int(self._x), int(self._y))
        if self._direction == Direction.LEFT:
            x -= 1
        elif self._direction == Direction.RIGHT:
            x += 1
        elif self._direction == Direction.UP:
            y -= 1
        elif self._direction == Direction.DOWN:
            y += 1

        return (x, y)

    @property
    def user_direction(self):
        return self._user_direction

    @user_direction.setter
    def user_direction(self, value):
        self._user_direction = value

