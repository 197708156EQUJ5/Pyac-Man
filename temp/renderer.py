import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import warnings
warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API",
    category=UserWarning,
)
import pygame

from maze import MazeManager
from utils.constants import Constants
from utils.resources import Utils
from utils.tile import Tile
from utils.tile_type import TileType
from utils.spritesheet_manager import SpritesheetManager

class Renderer():

    def __init__(self, maze: MazeManager):
        self._maze_manager: MazeManager = maze
        self._spritesheet_manager = SpritesheetManager()

    def draw(self, surface: pygame.Surface):
        for tile in self._maze_manager.maze:
            x = tile.col * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            y = tile.row * Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO
            w = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)
            h = Constants.TILE_SIZE * Constants.TILE_DISPLAY_RATIO - (tile.size * Constants.TILE_DISPLAY_RATIO)

            x += tile.size
            y += tile.size
            tile = self._spritesheet_manager.get_tile(tile)
            surface.blit(tile, (x, y))

if __name__ == "__main__":
    screen = pygame.display.set_mode((Constants.BOARD_WIDTH, Constants.BOARD_HEIGHT))
    clock = pygame.time.Clock()
    maze = MazeManager()
    renderer = Renderer(maze)
    while True:
        dt = clock.tick(Constants.FPS) / 1000.0
        screen.fill(Constants.BG_COLOR)
        renderer.draw(screen)
        pygame.display.flip()

