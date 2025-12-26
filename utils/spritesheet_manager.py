import json
import pygame
from typing import List

from utils.constants import Constants
from utils.tile import Tile

class SpritesheetManager():

    def __init__(self):
        self._spritesheet = pygame.image.load(Constants.SPRITESHEET_PATH).convert_alpha()
        self._tiles: List[pygame.Surface] = []
        self._wall_tiles = []
        self._load_tiles()
        self._sprite_tiles = {}

        file_name: str = Constants.TILE_MAP_PATH
        with open(file_name, 'r') as f:
            self._sprite_tiles = json.load(f)

    def _load_tiles(self):
        for row in range(0, Constants.SS_ROWS):
            for col in range(0, Constants.SS_COLS):
                src_rect = pygame.Rect(col * Constants.SS_TILE_SIZE, row * Constants.SS_TILE_SIZE, 
                    Constants.SS_TILE_SIZE, Constants.SS_TILE_SIZE)
                tile = self._spritesheet.subsurface(src_rect).copy()
                tile = pygame.transform.scale(tile, 
                    (Constants.SS_TILE_SIZE // 2, Constants.SS_TILE_SIZE // 2))
                self._tiles.append(tile)

    def get_tile(self, category, tile: Tile) -> pygame.Surface:
        try:
            col, row = self._sprite_tiles[category][tile.tile_type]['x'], self._sprite_tiles[category][tile.tile_type]['y']
            return self._tiles[row * Constants.SS_COLS + col]
        except KeyError:
            return self._tiles[6 * Constants.SS_COLS + 31]

