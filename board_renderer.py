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

    def draw(self, surface: pygame.Surface):
        
        for tile in self._maze_manager.maze:
            x = tile.col * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            y = tile.row * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            w = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)
            h = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)

            x += tile.size
            y += tile.size
            tile = self._spritesheet_manager.get_tile(tile)
            surface.blit(tile, (x, y))

        for entity in self._entities:
            origin_x = entity.x * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            origin_y = entity.y * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            r = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            pygame.draw.circle(surface, entity.color, (origin_x, origin_y), r)
