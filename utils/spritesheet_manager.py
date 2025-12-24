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
                #src_rect = pygame.Rect(col, row, Constants.TILE_SIZE * 2, Constants.TILE_SIZE * 2)
                src_rect = pygame.Rect(col * 48 + 1, row * 48 + 1, 46, 46)
                tile = self._spritesheet.subsurface(src_rect).copy()
                tile = pygame.transform.scale(tile, 
                    (Constants.SS_TILE_SIZE // 2, Constants.SS_TILE_SIZE // 2))
                self._tiles.append(tile)

    def get_tile_from(self, idx: int) -> pygame.Surface:
        return self._tiles[idx % len(self._tiles)]

    def get_tile(self, tile: Tile) -> pygame.Surface:

        if tile.wall_mask & 16:
            if tile.wall_mask == 90: # Northwest corner outer wall
                return self._tiles[4 * Constants.SS_COLS + 17]
            elif tile.wall_mask == 28: # North outer wall
                return self._tiles[4 * Constants.SS_COLS + 26]
            elif tile.wall_mask == 150: # Northeast corner outer wall
                return self._tiles[4 * Constants.SS_COLS + 16]
        else:
            if tile.wall_mask == 11:
                return self._tiles[3 * Constants.SS_COLS + 24]
            elif tile.wall_mask == 7:
                return self._tiles[3 * Constants.SS_COLS + 25]

            elif tile.wall_mask == 10:
                #return self._tiles[3 * Constants.SS_COLS + 23]
                return self._tiles[9 * Constants.SS_COLS + 9]
            elif tile.wall_mask == 12:
                return self._tiles[3 * Constants.SS_COLS + 20]
            elif tile.wall_mask == 6:
                #return self._tiles[3 * Constants.SS_COLS + 22]
                return self._tiles[9 * Constants.SS_COLS + 10]

        if tile.wall_mask & 32:
            if tile.wall_mask == 105:
                return self._tiles[4 * Constants.SS_COLS + 21]
            elif tile.wall_mask == 44:
                return self._tiles[4 * Constants.SS_COLS + 28]
            elif tile.wall_mask == 165:
                return self._tiles[4 * Constants.SS_COLS + 20]

        if tile.wall_mask & 64:
            if tile.wall_mask == 67:
                return self._tiles[4 * Constants.SS_COLS + 19]

        if tile.wall_mask & 128:
            if tile.wall_mask == 131:
                return self._tiles[4 * Constants.SS_COLS + 18]

        return  self._tiles[2 * Constants.SS_COLS + 0]

