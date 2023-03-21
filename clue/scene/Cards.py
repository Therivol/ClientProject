import pygame as p

from clue.scene.Scene import Scene
from gui.element.Button import Button
from util.Assets import Assets
from util.ClueUtil import ClueUtil
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class Cards(Scene):
    def __init__(self):
        super().__init__("CARDS")

        self.shadow = None

        self.back_button = Button(p.Rect(416, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.view_button = Button(p.Rect(416, 352, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.accuse_button = Button(p.Rect(416, 448, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.left_button = Button(p.Rect(224, 64, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.right_button = Button(p.Rect(672, 64, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.token_select = 0
        self.tokens = []

        self.room = ""

    def set_room(self, room):
        self.room = room

    def enter(self):
        self.token_select = 0
        self.tokens = [Scenes.get_scene("BOARD").tokens[index] for index in Scenes.get_scene("BOARD").players]


    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("PAUSE")

        if self.view_button.update():
            pass

        if self.accuse_button.update():
            pass

        if self.right_button.update() or Input.get_key_down(p.K_RIGHT):
            self.token_select += 1
            if self.token_select > len(self.tokens) - 1:
                self.token_select = 0

            print(Scenes.get_scene("BOARD").player_cards[self.token_select])

        if self.left_button.update() or Input.get_key_down(p.K_LEFT):
            self.token_select -= 1
            if self.token_select < 0:
                self.token_select = len(self.tokens) - 1

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)

        self.left_button.draw(surf)
        self.right_button.draw(surf)
        self.view_button.draw(surf)
        self.accuse_button.draw(surf)

        surf.blit(p.transform.scale(Assets.get_image(f"tokens/{self.tokens[self.token_select].token}.png", True), (192, 192)),
                (416, 64))

        return surf
