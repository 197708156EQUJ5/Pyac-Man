import pygame
from typing import List

from maze import MazeManager
from board_renderer import BoardRenderer
from entities import Entity
from entities import Pacman

class Board():

    def __init__(self):
        self._entities: List[Entity] = []
        self._entities.append(Pacman())
        self._maze: Maze = MazeManager()
        self._renderer = BoardRenderer(self._maze, self._entities)

    def update(self):
        for entity in self._entities:
            entity.move()

    def draw(self, surface: pygame.Surface):
        self._renderer.draw(surface)

