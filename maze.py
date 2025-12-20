from pathlib import Path

class Maze():

    def __init__(self):
        self.maze = self._from_file("assets/resources/maze_sheet")
        pass

    def _from_file(self, path: str | Path, encoding: str = "utf-8"):
        text = Path(path).read_text(encoding=encoding)
        print(f"{text}")

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

