from enum import Enum, auto

class TileType(Enum):

    WALL = auto()
    EMPTY = auto()
    PELLET = auto()
    POWER_PELLET = auto()
    DOOR = auto()
    TUNNEL = auto()
