import pygame as p

from clue.Player import Player
from clue.scene.Scene import Scene
from gui.element.Button import Button
from gui.element.Select import Select
from util.Assets import Assets
from util.GameInstance import GameInstance
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class CreatePlayer(Scene):
    def __init__(self):
        super().__init__("CREATE PLAYER")

        self.shadow = None

        self.back_button = Button(p.Rect(64, 672, 192, 64), (0, 0, 0), (50, 50, 50))
        self.next_button = Button(p.Rect(768, 672, 192, 64), (0, 0, 0), (50, 50, 50))

        self.token_buttons = []

        self.character_select = None
        self.player = None

    def enter(self):
        self.player = Player("1", (0, 0), "MISS SCARLET")

        x = 48
        for _ in range(6):
            button = Select(p.Rect(x, 128, 128, 128), (0, 0, 0), (100, 100, 100), idle_border=(150, 150, 150),
                            active_border=(150, 150, 150))
            self.token_buttons.append(button)
            x += 160

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("ADD PLAYERS")

        if self.character_select and self.next_button.update():
            Scenes.set_scene("ADD PLAYERS")
            GameInstance.add_player(self.player)

        for button in self.token_buttons:
            button.update()

        self.character_select = None
        for i, button in enumerate(self.token_buttons):
            if button.pressed:
                self.character_select = i + 1
                break

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)


        if self.character_select:
            self.next_button.draw(surf)

        for button in self.token_buttons:
            button.draw(surf)

        return surf
