import json

from gui.element.Button import Button
from gui.element.Select import Select
from util.Assets import Assets
from util.GameInstance import GameInstance
from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Globals import Globals
from clue.scene.Scene import Scene
from clue.Player import Player
import pygame as p


class AddPlayers(Scene):
    def __init__(self):
        super().__init__("ADD PLAYERS")

        self.buttons = []
        self.selects = []
        self.back_button = Button(p.Rect(144, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  active_border=(174, 174, 174))

        self.remove_button = Button(p.Rect(400, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                    active_border=(174, 174, 174))

        self.next_button = Button(p.Rect(656, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  active_border=(174, 174, 174))

        self.selected = -1

    def awake(self):
        x, y = 0, 32
        for i in range(6):
            x = (i % 3) * 256 + 128
            if i > 2:
                y = 354
            button = Button(p.Rect(x, y, 224, 288), (96, 123, 92), (136, 163, 132),
                            active_border=(174, 174, 174))
            self.buttons.append(button)

            select = Select(p.Rect(x, y, 224, 288), (100, 100, 100), (150, 150, 150),
                            active_border=(174, 174, 174), sensitive=True)
            self.selects.append(select)

    def update(self):
        if Input.get_key_down(p.K_SPACE):
            self.back_button.toggle_disabled()

        if self.back_button.update():
            Scenes.set_scene("MENU")

        if self.selected >= 0:
            if self.remove_button.update():
                GameInstance.remove_player(GameInstance.players[self.selected])
                self.selected = -1

        if GameInstance.num_players() >= 3 and self.next_button.update():
            Scenes.set_scene("BOARD")

        self.selected = -1
        for i in range(6):
            if GameInstance.players[i]:
                if self.selects[i].update():
                    self.selected = i
            else:
                if self.buttons[i].update():
                    Scenes.set_scene("CREATE PLAYER")
                    self.selects[i].pressed = False
                break

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        add_img = Assets.get_image("ui/plus.png", alpha=True)
        for i in range(6):
            if GameInstance.players[i]:
                select = self.selects[i]
                select.draw(surf)
            else:
                button = self.buttons[i]
                button.draw(surf)
                pos = Assets.position_by_percent(add_img.get_size(), button.rect.size, (0.5, 0.5))
                pos = pos[0] + button.rect.left, pos[1] + button.rect.top
                surf.blit(add_img, pos)
                break

        if self.selected >= 0:
            self.remove_button.draw(surf)

        if GameInstance.num_players() >= 3:
            self.next_button.draw(surf)

        self.back_button.draw(surf)

        return surf
