import json

from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from clue.scene.Scene import Scene
import pygame as p


class Menu(Scene):
    def __init__(self):
        super().__init__("MENU")
        self.board = [[]]
        self.TILE_SIZE = 0

    def awake(self):
        with open("assets/board/board.json", "r") as file:
            self.board = json.load(file)

        self.TILE_SIZE = Settings.get("TILE SIZE")

    def update(self):
        if Input.get_key_down(p.K_RETURN):
            Scenes.set_scene("BOARD")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill((0, 0, 0))

        return surf
