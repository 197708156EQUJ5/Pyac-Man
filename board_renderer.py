import pygame
from typing import List

from entities.entity import Entity
from maze import MazeManager
from utils.color import Color
from utils.constants import Constants
from utils.resources import Utils
from utils.tile import Tile
from utils.tile_type import TileType

class BoardRenderer():

    FONT_PATH = Utils.resource_path("assets/fonts/ttf/JetBrainsMono-Regular.ttf")
    
    def __init__(self, maze: MazeManager, entities: List[Entity]):
        self.font = pygame.font.Font(self.FONT_PATH, 18)
        self._maze_manager: MazeManager = maze
        self._entities: List[Entity] = entities

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
            elif tile.tile_type == TileType.EMPTY:
                x += tile.size
                y += tile.size
                pygame.draw.rect(surface, Color.BLACK, (x, y, w, h))
#            elif tile.tile_type == TileType.WALL_ONE:
#                text = self.font.render("NW", True, Color.BLUE)
#                surface.blit(text, (x, y))
            else:
                x += tile.size
                y += tile.size
                pygame.draw.rect(surface, tile.color, (x, y, w, h))

        for entity in self._entities:
            origin_x = entity.x * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            origin_y = entity.y * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            r = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            pygame.draw.circle(surface, entity.color, (origin_x, origin_y), r)
