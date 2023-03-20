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


class CreatePlayer(Scene):
    def __init__(self):
        super().__init__("CREATE PLAYER")

        self.shadow = None

        self.back_button = Button(p.Rect(64, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.next_button = Button(p.Rect(768, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  disable_color=(0, 0, 0))

        self.token_buttons = []

        self.token_select = None
        self.player = None

    def enter(self):

        for button in self.token_buttons:
            button.pressed = False

        self.next_button.set_disabled(True)
        self.token_select = None
        self.player = Player("1", (0, 0), "MISS SCARLET")

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

        x = 48
        for _ in range(6):
            button = Select(p.Rect(x, 128, 128, 128), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
            self.token_buttons.append(button)
            x += 160

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("ADD PLAYERS")

        if self.next_button.update():
            self.player.token = ClueUtil.characters[self.token_select]
            print(self.player.token)
            Scenes.set_scene("ADD PLAYERS")
            Scenes.get_scene("ADD PLAYERS").add_player(self.player)

        for button in self.token_buttons:
            button.update()

        for i, button in enumerate(self.token_buttons):
            if button.pressed and self.token_select != i:
                self.token_select = i
                break

        for i, button in enumerate(self.token_buttons):
            if i != self.token_select:
                button.pressed = False

        for button in self.token_buttons:
            if button.pressed:
                break

        else:
            self.token_select = None

        self.next_button.set_disabled(self.token_select is None)

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)

        self.next_button.draw(surf)

        for button in self.token_buttons:
            button.draw(surf)

        return surf
