import pygame

from maze import MazeManager
from board_renderer import BoardRenderer
#from entities import Pacman

class Board():

    def __init__(self):
        self._maze: Maze = MazeManager()
        self._renderer = BoardRenderer(self._maze)

    def draw(self, surface: pygame.Surface):
        self._renderer.draw(surface)

