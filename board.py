import math
import pygame
from typing import List

from maze import MazeManager
from board_renderer import BoardRenderer
from entities.entity import Entity
from entities.pacman import Pacman
from entities.ghost import Ghost
from utils.constants import EntityConstants, Pinky, Inky, Blinky, Clyde
from utils.direction import Direction

class Board():

    EPS = 1e-6

    def __init__(self):
        self._entities: List[Entity] = []
        self._pacman = Pacman()
        self._entities.append(self._pacman)
#        self._entities.append(Ghost(Pinky()))
#        self._entities.append(Ghost(Inky()))
#        self._entities.append(Ghost(Blinky()))
#        self._entities.append(Ghost(Clyde()))
        self._maze: Maze = MazeManager()
        self._renderer = BoardRenderer(self._maze, self._entities)

    def change_direction(self, direction: Direction):
        self._pacman.user_direction = direction

    def update(self, dt):

        for entity in self._entities:
            step = entity.get_speed() * dt
            if entity is self._pacman:
                self._try_turn(step)

            next_col, next_row = entity.next_cell()

            if self._can_move((next_col, next_row)):
                prev_pos = (entity.x, entity.y)
                entity.move(dt)
                curr_pos = (entity.x, entity.y)
                self._is_pellet_eaten(prev_pos, curr_pos)
                continue

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

    def _is_pellet_eaten(self, prev_pos: tuple[float, float], curr_pos: tuple[float, float]) -> bool:
        col = curr_pos[0]
        row = curr_pos[1]
        if not self._maze.has_pellet(int(col), int(row)):
            return

        if self._pacman.direction == Direction.RIGHT or self._pacman.direction == Direction.DOWN:
            if prev_pos[0] <= int(col) + 0.5 <= col and prev_pos[1] <= int(row) + 0.5 <= row:
                self._maze.consume_pellet(col, row)
        elif self._pacman.direction == Direction.LEFT or self._pacman.direction == Direction.UP:
            if col <= int(col) + 0.5 <= prev_pos[0] and row <= int(row) + 0.5 <= prev_pos[1]:
                self._maze.consume_pellet(col, row)

    def draw(self, surface: pygame.Surface):
        self._renderer.draw(surface)

    def _can_move(self, pos: tuple) -> bool:
        return not self._maze.is_wall(pos[0], pos[1])

    def _near_centerline(self, v: float) -> bool:
        return abs(v - (math.floor(v) + 0.5)) < self.EPS

    def _can_turn(self, desired_dir) -> bool:
        # turning to horizontal requires being centered vertically, and vice versa
        if desired_dir in (Direction.LEFT, Direction.RIGHT):
            if not self._near_centerline(self._pacman.y):
                return False
        elif desired_dir in (Direction.UP, Direction.DOWN):
            if not self._near_centerline(self._pacman.x):
                return False

        # also must have an open cell in that desired direction
        col = math.floor(self._pacman.x)
        row = math.floor(self._pacman.y)

        if desired_dir == Direction.LEFT:  target = (col - 1, row)
        if desired_dir == Direction.RIGHT: target = (col + 1, row)
        if desired_dir == Direction.UP:    target = (col, row - 1)
        if desired_dir == Direction.DOWN:  target = (col, row + 1)

        return not self._maze.is_wall(target[0], target[1])

    def _cell_center(self, v: float) -> float:
        return math.floor(v) + 0.5

    def _dist_to_center(self, v: float) -> float:
        return abs(v - self._cell_center(v))

    def _is_horizontal(self, d: Direction) -> bool:
        return d in (Direction.LEFT, Direction.RIGHT)

    def _is_vertical(self, d: Direction) -> bool:
        return d in (Direction.UP, Direction.DOWN)

    def _next_cell_from(self, x: float, y: float, d: Direction) -> tuple[int, int]:
        col = math.floor(x)
        row = math.floor(y)
        if d == Direction.LEFT:  return (col - 1, row)
        if d == Direction.RIGHT: return (col + 1, row)
        if d == Direction.UP:    return (col, row - 1)
        if d == Direction.DOWN:  return (col, row + 1)
        return (col, row)

    def _try_turn(self, step: float) -> None:
        desired = self._pacman.user_direction
        current = self._pacman.direction

        if desired == current or desired == Direction.NONE:
            return

        # must be open in desired direction
        col, row = self._next_cell_from(self._pacman.x, self._pacman.y, desired)
        if self._maze.is_wall(col, row):
            return

        # perpendicular turn?
        if (self._is_horizontal(desired) and self._is_vertical(current)) or (self._is_vertical(desired) and self._is_horizontal(current)):
            # must be centered on the perpendicular axis already (stay in your lane)
            if self._is_horizontal(desired):
                if self._dist_to_center(self._pacman.y) > (step + self.EPS):
                    return
                # snap into the intersection lane
                self._pacman._y = self._cell_center(self._pacman.y)
                # and if we're close enough to the intersection center, snap X too
                if self._dist_to_center(self._pacman.x) <= (step + self.EPS):
                    self._pacman._x = self._cell_center(self._pacman.x)
            else:
                if self._dist_to_center(self._pacman.x) > (step + self.EPS):
                    return
                self._pacman._x = self._cell_center(self._pacman.x)
                if self._dist_to_center(self._pacman.y) <= (step + self.EPS):
                    self._pacman._y = self._cell_center(self._pacman.y)

            self._pacman.direction = desired
            return

        # same-axis change (LEFT<->RIGHT or UP<->DOWN) can be immediate if open
        self._pacman.direction = desired
