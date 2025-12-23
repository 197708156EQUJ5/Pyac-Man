from pathlib import Path
from typing import List

from utils import Constants
from utils import Color
from utils import Tile
from utils import TileType

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

#        for tile in self._maze:
#            if tile.tile_type == TileType.WALL:
#                col = tile.col
#                row = tile.row


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

        return Tile(tile_type, size, color)

    def _get_wall_type(self, col: int, row: int) -> TileType:
        c = int(col)
        r = int(row)
        if c == 0:
            if self._get_tile(c, r - 1).tile_type == TileType.EMPTY:
                return TileType.WALL_ONW

        return TileType.WALL

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

    def _get_tile(self,  col: int, row: int) -> Tile:
        return self._maze[int(row) * Constants.COLUMN_COUNT + int(col)]

    def is_tunnel(self, col: int, row: int) -> bool:
        return False

    def consume_pellet(self, col: int, row: int):
        pass

