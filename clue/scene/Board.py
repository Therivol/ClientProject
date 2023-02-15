import json

from util.Settings import Settings
from clue.scene.Scene import Scene
import pygame as p


class Board(Scene):
    def __init__(self):
        super().__init__("BOARD")
        self.board = [[]]
        self.TILE_SIZE = 0

    def awake(self):
        with open("assets/board/board.json", "r") as file:
            self.board = json.load(file)

        self.TILE_SIZE = Settings.get("TILE SIZE")

    def update(self):
        pass

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill((255, 255, 255))

        y = 0
        for row in self.board:
            x = 0
            for tile in row:
                color = (0, 0, 0)
                if tile == 0:
                    color = (0, 0, 0)
                elif tile == 1:
                    color = (200, 200, 200)
                elif tile == 2:
                    color = (209, 185, 128)
                elif tile == 3:
                    color = (125, 150, 125)
                elif tile == 4:
                    color = (125, 125, 150)
                x_pos, y_pos = x * self.TILE_SIZE, y * self.TILE_SIZE
                p.draw.rect(surf, color, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE))
                if tile == 2 or tile == 0:
                    p.draw.rect(surf, (0, 0, 0), (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE), 1)
                x += 1
            y += 1

        return surf
