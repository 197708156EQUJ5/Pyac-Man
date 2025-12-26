import json
from pathlib import Path
from typing import List, NamedTuple

from utils.constants import Constants
from utils.tile import Tile
from utils.tile_type import TileType

class MazeManager():

    def __init__(self):
        self._maze: List[Tile] = []

        file_name: str = Constants.MAZE_SHEET_PATH
        with open(file_name, "r", encoding="utf-8") as f:
            for row, line in enumerate(f):
                line = line.rstrip("\n")
                if not line:
                    continue
                for col, ch in enumerate(line):
                    self._maze.append(Tile(ch, col, row))

    @property
    def maze(self) -> List[Tile]:
        return self._maze

    def _is_off(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == '-'
    
    def is_wall(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type.isalpha()

    def has_pellet(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == '^'

    def has_power_pellet(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == '&'

    def _get_tile(self, col: int, row: int) -> Tile:
        return self._maze[int(row) * Constants.COLUMN_COUNT + int(col)]

    def is_tunnel(self, col: int, row: int) -> bool:
        return False

    def consume_pellet(self, col: int, row: int):
        tile = self._get_tile(col, row)
        if tile:
            tile.tile_type = '_'

