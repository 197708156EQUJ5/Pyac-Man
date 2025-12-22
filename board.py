import math
import pygame
from typing import List

from maze import MazeManager
from board_renderer import BoardRenderer
from entities import Entity
from entities import Pacman
from entities import Ghost
from utils import EntityConstants, Pinky, Inky, Blinky, Clyde
from utils import Direction

class Board():

    EPS = 1e-6

    def __init__(self):
        self._entities: List[Entity] = []
        self._pacman = Pacman()
        self._entities.append(self._pacman)
        self._entities.append(Ghost(Pinky()))
#        self._entities.append(Ghost(Inky()))
#        self._entities.append(Ghost(Blinky()))
#        self._entities.append(Ghost(Clyde()))
        self._maze: Maze = MazeManager()
        self._renderer = BoardRenderer(self._maze, self._entities)

    def change_direction(self, direction: Direction):
        if direction != self._pacman.direction:
            if self._can_turn(self._pacman, self._maze, direction):
                self._pacman.direction = direction

    def update(self, dt):

        for entity in self._entities:
            next_col, next_row = entity.next_cell()

            if self._can_move((next_col, next_row)):
                entity.move(dt)
                continue

            step = entity.get_speed() * dt

            if entity.direction == Direction.LEFT:
                target = math.floor(entity.x) + 0.5
                entity._x = max(target, entity.x - step)
                if entity._x <= target + self.EPS:
                    entity._x = target
                    entity.direction = Direction.NONE

            elif entity.direction == Direction.RIGHT:
                target = math.floor(entity.x) + 0.5
                entity._x = min(target, entity.x + step)
                if entity._x >= target - self.EPS:
                    entity._x = target
                    entity.direction = Direction.NONE

            elif entity.direction == Direction.UP:
                target = math.floor(entity.y) + 0.5
                entity._y = max(target, entity.y - step)
                if entity._y <= target + self.EPS:
                    entity._y = target
                    entity.direction = Direction.NONE

            elif entity.direction == Direction.DOWN:
                target = math.floor(entity.y) + 0.5
                entity._y = min(target, entity.y + step)
                if entity._y >= target - self.EPS:
                    entity._y = target
                    entity.direction = Direction.NONE

            else:
                # Direction.NONE
                pass

    def draw(self, surface: pygame.Surface):
        self._renderer.draw(surface)

    def _can_move(self, pos: tuple) -> bool:
        return not self._maze.is_wall(pos[0], pos[1])

    def _near_centerline(self, v: float) -> bool:
        return abs(v - (math.floor(v) + 0.5)) < self.EPS

    def _can_turn(self, pacman, maze, desired_dir) -> bool:
        # turning to horizontal requires being centered vertically, and vice versa
        if desired_dir in (Direction.LEFT, Direction.RIGHT):
            if not self._near_centerline(pacman.y):
                return False
        elif desired_dir in (Direction.UP, Direction.DOWN):
            if not self._near_centerline(pacman.x):
                return False

        # also must have an open cell in that desired direction
        col = math.floor(pacman.x)
        row = math.floor(pacman.y)

        if desired_dir == Direction.LEFT:  target = (col - 1, row)
        if desired_dir == Direction.RIGHT: target = (col + 1, row)
        if desired_dir == Direction.UP:    target = (col, row - 1)
        if desired_dir == Direction.DOWN:  target = (col, row + 1)

        return not maze.is_wall(target[0], target[1])

