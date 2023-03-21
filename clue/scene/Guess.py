import pygame as p

from clue.Player import Player
from clue.scene.Scene import Scene
from gui.element.Button import Button
from gui.element.Select import Select
from util.Assets import Assets
from util.ClueUtil import ClueUtil
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class Guess(Scene):
    def __init__(self):
        super().__init__("GUESS")

        self.shadow = None

        self.back_button = Button(p.Rect(64, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.next_button = Button(p.Rect(768, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  disable_color=(0, 0, 0))

        self.left_button = Button(p.Rect(224, 128, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.right_button = Button(p.Rect(672, 128, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.token_select = 0
        self.tokens = []

        self.room = ""

    def set_room(self, room):
        self.room = room

    def enter(self):
        self.token_select = 0
        self.tokens = ClueUtil.characters()

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("BOARD")

        if self.next_button.update() or Input.get_key_down(p.K_RETURN):
            print(self.tokens[self.token_select])
            Scenes.set_scene("BOARD")
            Scenes.get_scene("BOARD").add_to_room(self.room, self.tokens[self.token_select])
            Scenes.get_scene("BOARD").guess_button.set_disabled(True)

        if self.right_button.update() or Input.get_key_down(p.K_RIGHT):
            self.token_select += 1
            if self.token_select > len(self.tokens) - 1:
                self.token_select = 0

        if self.left_button.update() or Input.get_key_down(p.K_LEFT):
            self.token_select -= 1
            if self.token_select < 0:
                self.token_select = len(self.tokens) - 1

        self.next_button.set_disabled(self.token_select is None)

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)

        self.next_button.draw(surf)

        self.left_button.draw(surf)
        self.right_button.draw(surf)

        surf.blit(p.transform.scale(Assets.get_image(f"tokens/{self.tokens[self.token_select]}.png", True), (192, 192)),
                (416, 128))

        return surf
