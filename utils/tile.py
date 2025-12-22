
from utils import Color

class Tile():

    LARGE = 0
    MEDIUM = 1
    SMALL = 2
    EXTRA_SMALL = 3

    def __init__(self, tile_type, size: int, color):
        self._col = 0
        self._row = 0
        self._tile_type = tile_type
        self._size = size
        self._color = color

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self._col = value

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def tile_type(self):
        return self._tile_type

    @tile_type.setter
    def tile_type(self, value):
        self._tile_type = value

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color
