import pygame
from typing import List

from entities.entity import Entity
from maze import MazeManager
from utils.color import Color
from utils.constants import Constants
from utils.resources import Utils
from utils.tile import Tile
from utils.tile_type import TileType
from utils.spritesheet_manager import SpritesheetManager

class BoardRenderer():

    FONT_PATH = Utils.resource_path(Constants.FONT_PATH)
    
    def __init__(self, maze: MazeManager, entities: List[Entity]):
        self.font = pygame.font.Font(self.FONT_PATH, 18)
        self._maze_manager: MazeManager = maze
        self._entities: List[Entity] = entities
        self._spritesheet_manager = SpritesheetManager()
        self.flag = False

    def draw(self, surface: pygame.Surface):
        self.flag = False
        pygame.draw.rect(surface, Color.WHITE, (0, 0, Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO, Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO), 1, border_radius=1)
        for idx, maze_tile in enumerate(self._maze_manager.maze):
            x = maze_tile.col * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            y = maze_tile.row * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            tile = self._spritesheet_manager.get_tile('wall', maze_tile)
            surface.blit(tile, (x, y))

        for entity in self._entities:
            origin_x = entity.x * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            origin_y = entity.y * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            r = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            pygame.draw.circle(surface, Color.YELLOW, (origin_x, origin_y), r)


