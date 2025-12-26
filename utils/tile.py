
class Tile():

    def __init__(self, tile_type: str, col: int, row: int):
        self._col = col
        self._row = row
        self._tile_type = tile_type

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
