import math

from utils import Color

class Constants():

    TILE_DISPLAY_RATIO = 3
    BOARD_WIDTH = 224 * TILE_DISPLAY_RATIO
    BOARD_HEIGHT = 288 *TILE_DISPLAY_RATIO
    SS_COLS = 32
    SS_ROWS = 20
    TILE_SIZE = 8
    TILE_ROW_COUNT = 3
    COLUMN_COUNT = 28
    ROW_COUNT = 36
    SPRITESHEET_PATH = 'assets/images/pacman-spritesheet.png'
    
    BG_COLOR = (0, 0, 0)
    FPS = 60.606061
    KEY_REPEAT_DELAY = 400      # ms
    KEY_REPEAT_INTERVAL = 50    # ms

# Entity Related Constants
class EntityConstants():
    INIT = (0,0)
    BASE_SPEED = 7.57575
    COLOR = Color.BLACK

class PacmanConstants(EntityConstants):
    INIT = (14, 26.5)
    COLOR = Color.YELLOW

class Blinky(EntityConstants):
    INIT = (14, 14.5)
    COLOR = Color.RED

class Inky():
    INIT = (12, 17.5)
    COLOR = Color.TEAL

class Pinky():
    INIT = (14, 17.5)
    COLOR = Color.PINK

class Clyde():
    INIT = (16, 17.5)
    COLOR = Color.ORANGE

