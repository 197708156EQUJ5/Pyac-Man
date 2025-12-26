import json
from pathlib import Path
from typing import List, NamedTuple

from utils.color import Color
from utils.constants import Constants
from utils.tile import Tile
from utils.tile_type import TileType

class SpriteTile(NamedTuple):
    key: tuple[int,int]
    col: int
    row: int

class MazeManager():

    def __init__(self):
        self._maze: List[Tile] = []
        self._walls: List[SpriteTile] = []

        file_name: str = Constants.TILE_MAP_PATH
        with open(file_name, 'r') as f:
            data = json.load(f)

        file_name: str = Constants.MAZE_SHEET_PATH
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

        file_name: str = Constants.WALL_SHEET_PATH
        with open(file_name, "r", encoding="utf-8") as f:
            for row, line in enumerate(f):
                line = line.rstrip("\n")
                if not line:
                    continue
                for col, ch in enumerate(line):
                    if not ch == '.' and not ch == '#':
                        self._get_tile(col, row).wall_mask = (data[ch]['x'],data[ch]['y'])

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

    @property
    def maze(self) -> List[Tile]:
        return self._maze

    def _is_off(self, col: int, row: int) -> bool:
        tile = self._get_tile(col, row)
        return tile.tile_type == TileType.OFF
    
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

