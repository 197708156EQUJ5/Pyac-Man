from entities import Entity
from utils import Color
from utils import EntityConstants
from utils import Direction

class Ghost(Entity):

    def __init__(self, ghost_constants: EntityConstants):
        super().__init__(ghost_constants.INIT[0], ghost_constants.INIT[1], color=ghost_constants.COLOR)

    def move(self, dt):
        if self._direction == Direction.LEFT:
            self._x -= dt * EntityConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.RIGHT:
            self._x += dt * EntityConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.UP:
            self._y -= dt * EntityConstants.BASE_SPEED * self._mode
        elif self._direction == Direction.DOWN:
            self._y += dt * EntityConstants.BASE_SPEED * self._mode

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
