#!/usr/bin/env python3

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import warnings
warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API",
    category=UserWarning,
)
import pygame

from board import Board
from utils import Constants
from utils import Direction

class App:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((Constants.BOARD_WIDTH, Constants.BOARD_HEIGHT))
        pygame.display.set_caption("Pac-man")
#        app_icon = pygame.image.load(Utils.resource_path("assets/icons/app_icon.png")).convert_alpha()
#        pygame.display.set_icon(app_icon)
        pygame.key.set_repeat(Constants.KEY_REPEAT_DELAY, Constants.KEY_REPEAT_INTERVAL)

        self.clock = pygame.time.Clock()
        self.is_running = True
        self.elapsed_time = 0.0
        self.display_time = 0.0
        self.time_accumulator = 0.0

        self.board = Board()

    def run(self):
        while self.is_running:
            dt = self.clock.tick(Constants.FPS) / 1000.0
            self.elapsed_time += dt
            self.update(dt)
            self.handle_events()
            self.draw()
        pygame.quit()

    def quit(self):
        self.is_running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                # ESC quits for now
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                self.handle_key_down(event)

    def handle_key_down(self, event: pygame.event.Event):
        can_move = True
        if event.key == pygame.K_LEFT:
            self.pacman.move(Direction.LEFT)
        elif event.key == pygame.K_RIGHT:
            self.pacman.move(Direction.RIGHT)
        elif event.key == pygame.K_DOWN:
            can_move = self.pacman.move(Direction.DOWN)
        elif event.key == pygame.K_UP:
            can_move = self.pacman.move(Direction.UP)

        if not can_move:
            pass

    def update(self, dt: float):
        self.board.update(dt)

    def draw(self):
        # Fill screen with background 0,0,0
        self.screen.fill(Constants.BG_COLOR)

        # Draw UI
        self.board.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.run()
