from entities import Entity
from utils import Color
from utils import PacmanConstants
from utils import Direction

class Pacman(Entity):

    def __init__(self):
        super().__init__(PacmanConstants.INIT[0], PacmanConstants.INIT[1], color=Color.YELLOW)

    def move(self, dt):
        pixels_moved = dt * PacmanConstants.BASE_SPEED * self._mode * 8
        print(f"{pixels_moved}")
        if self._direction == Direction.LEFT:
            self._x -= dt * PacmanConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.RIGHT:
            self._x += dt * PacmanConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.UP:
            self._y -= dt * PacmanConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.DOWN:
            self._y += dt * PacmanConstants.BASE_SPEED * self._mode
