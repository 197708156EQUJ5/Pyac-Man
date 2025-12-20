import pygame

from maze import MazeManager
from utils import Constants
from utils import TileType

class BoardRenderer():

    def __init__(self, maze: MazeManager):
        self._maze_manager: MazeManager = maze

    def draw(self, surface: pygame.Surface):
        size = 0
        for tile in self._maze_manager.maze:
            x = tile.col * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            y = tile.row * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            w = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)
            h = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)
            if tile.tile_type == TileType.PELLET or tile.tile_type == TileType.POWER_PELLET:
                origin_x = x + (Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO // 2)
                origin_y = y + (Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO // 2)
                pygame.draw.circle(surface, tile.color, (origin_x, origin_y), w // 2)
            else:
                x += tile.size
                y += tile.size
                pygame.draw.rect(surface, tile.color, (x, y, w, h))

