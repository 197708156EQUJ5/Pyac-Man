from entities import Entity
from utils import Color

class Pacman(Entity):

    def __init__(self):
        super().__init__(14, 26.5, color=Color.YELLOW)
