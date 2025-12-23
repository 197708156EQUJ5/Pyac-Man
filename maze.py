from pathlib import Path
from typing import List

from utils.color import Color
from utils.constants import Constants
from utils.tile import Tile
from utils.tile_type import TileType

class MazeManager():

    def __init__(self):
        self._maze: List[Tile] = []

        file_name: str = "assets/resources/maze_sheet"
        with open(file_name, "r", encoding="utf-8") as f:
            for row, line in enumerate(f):
                line = line.rstrip("\n")
                if not line:
                    continue
                for col, tile_ch in enumerate(line):
                    tile: Tile = self._calculate_tile(tile_ch, col, row)
                    tile.row = row
                    tile.col = col
                    self._maze.append(tile)

        for tile in self._maze:
            if tile.tile_type == TileType.WALL:
                col = tile.col
                row = tile.row
                tile.wall_mask = self._create_wall_mask(col, row)

    def _calculate_tile(self, tile: str, col: int, row: int) -> Tile:
        color: Color = Color.BLACK
        size: int = Tile.LARGE
        tile_type: TileType = TileType.EMPTY

        if tile == '#':
            color = Color.BLUE
            size = Tile.LARGE
            tile_type = TileType.WALL
        elif tile == '^':
            color = Color.OFF_WHITE
            size = Tile.EXTRA_SMALL
            tile_type = TileType.PELLET
        elif tile == '&':
            color = Color.PURPLE
            size = Tile.MEDIUM
            tile_type = TileType.POWER_PELLET
        elif tile == '+':
            color = Color.PINK
            size = Tile.SMALL
            tile_type = TileType.DOOR
        elif tile == '=':
            color = Color.BLACK
            size = Tile.SMALL
            tile_type = TileType.TUNNEL
        elif tile == '-':
            color = Color.BLACK
            size = Tile.SMALL
            tile_type = TileType.OFF

        return Tile(tile_type, size, color)

    def _create_wall_mask(self, col, row):
        rows = Constants.ROW_COUNT
        cols = Constants.COLUMN_COUNT

        mask = 0
        bit_0 = 0
        bit_1 = 0
        bit_2 = 0
        bit_3 = 0
        bit_4 = 0

        # North
        if row > 0 and self.is_wall(col, row - 1):
            bit_0 = 1
            mask |= 1

        # South
        if row < rows - 1 and self.is_wall(col, row + 1):
            bit_1 = 1
            mask |= 2

        # East
        if col > 0 and self.is_wall(col - 1, row):
            bit_2 = 1
            mask |= 4

        # West
        if col < cols - 1 and self.is_wall(col + 1, row):
            bit_3 = 1
            mask |= 8

#        if row < 0 and row > rows - 1:
#            return mask
        
        for r in range(-1, 1):
            for c in range(-1, 1):
                if col + c < 0 or col + c > cols - 1 or row + r < 0 or row + c > rows - 1:
                    bit_4 = 1
                    mask |= 16
                elif self._get_tile(col + c, row + r).tile_type == TileType.OFF:
                    bit_4 = 1
                    mask |= 16

        if row == 33:
            print(f"{col},{row} mask: {mask} {bit_4}{bit_3}{bit_2}{bit_1}{bit_0}")
        return mask

    @property
    def maze(self) -> List[Tile]:
        return self._maze
    
    def is_wall(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == TileType.WALL

    def has_pellet(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == TileType.PELLET

    def has_power_pellet(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == TileType.POWER_PELLET

    def delicious(self, col: int, row: int):
        tile = self._get_tile(col, row)
        if tile:
            tile.tile_type = TileType.EMPTY

    def _get_tile(self, col: int, row: int) -> Tile:
        return self._maze[int(row) * Constants.COLUMN_COUNT + int(col)]

    def is_tunnel(self, col: int, row: int) -> bool:
        return False

    def consume_pellet(self, col: int, row: int):
        pass

