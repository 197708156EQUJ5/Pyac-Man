import pygame
from typing import List

from maze import MazeManager
from board_renderer import BoardRenderer
from entities import Entity
from entities import Pacman
from entities import Ghost
from utils import EntityConstants, Pinky, Inky, Blinky, Clyde

class Board():

    def __init__(self):
        self._entities: List[Entity] = []
        self._entities.append(Pacman())
        self._entities.append(Ghost(Pinky()))
        self._entities.append(Ghost(Inky()))
        self._entities.append(Ghost(Blinky()))
        self._entities.append(Ghost(Clyde()))
        self._maze: Maze = MazeManager()
        self._renderer = BoardRenderer(self._maze, self._entities)

    def update(self, dt):
        for entity in self._entities:
            #pass
            entity.move(dt)

    def draw(self, surface: pygame.Surface):
        self._renderer.draw(surface)

