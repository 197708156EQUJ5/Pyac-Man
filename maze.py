from pathlib import Path
from typing import List

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
                    tile: Tile = self._calculate_tile(tile_ch)
                    tile.row = row
                    tile.col = col
                    self._maze.append(tile)

    def _calculate_tile(self, tile: str) -> Tile:
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

    @property
    def maze(self) -> List[Tile]:
        return self._maze
    
    def is_wall(self, col: int, row: int) -> bool:
        return False

    def has_pellet(self, col: int, row: int) -> bool:
        return False

    def has_power_pellet(self, col: int, row: int) -> bool:
        return False

    def is_tunnel(self, col: int, row: int) -> bool:
        return False

    def consume_pellet(self, col: int, row: int):
        pass

