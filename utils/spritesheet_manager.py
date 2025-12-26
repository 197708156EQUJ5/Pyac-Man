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

    def _load_tiles(self):
        for row in range(0, Constants.SS_ROWS):
            for col in range(0, Constants.SS_COLS):
                src_rect = pygame.Rect(col * Constants.SS_TILE_SIZE, row * Constants.SS_TILE_SIZE, 
                    Constants.SS_TILE_SIZE, Constants.SS_TILE_SIZE)
                tile = self._spritesheet.subsurface(src_rect).copy()
                tile = pygame.transform.scale(tile, 
                    (Constants.SS_TILE_SIZE // 2, Constants.SS_TILE_SIZE // 2))
                self._tiles.append(tile)

    def get_tile(self, tile: Tile) -> pygame.Surface:
        return self._tiles[tile.wall_mask[1] * Constants.SS_COLS + tile.wall_mask[0]]

