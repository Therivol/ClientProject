import json

from gui.element.Button import Button
from util.Assets import Assets
from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Globals import Globals
from clue.scene.Scene import Scene
import pygame as p


class AddPlayers(Scene):
    def __init__(self):
        super().__init__("ADD PLAYERS")

        self.players = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        self.buttons = []
        self.back_button = Button(p.Rect(144, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  active_border=(174, 174, 174))

        self.remove_button = Button(p.Rect(400, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  active_border=(174, 174, 174))

        self.next_button = Button(p.Rect(656, 688, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  active_border=(174, 174, 174))
        self.selected = None

    def awake(self):
        x, y = 0, 32
        for i in range(6):
            x = (i % 3) * 256 + 128
            if i > 2:
                y = 354
            button = Button(p.Rect(x, y, 224, 288), (96, 123, 92), (136, 163, 132),
                            active_border=(174, 174, 174))
            self.buttons.append(button)

    def add_player(self, player, slot):
        self.players[slot] = player

    def remove_player(self, slot):
        del self.players[slot]

    def update(self):
        if self.back_button.update():
            Scenes.set_scene("MENU")

        if self.selected:
            if self.remove_button.update():
                del self.players[self.selected]
                self.selected = None

        if self.next_button.update():
            num_players = len([player for player in self.players.values() if player is not None])
            if num_players > -1:
                Scenes.set_scene("BOARD")

        for button in self.buttons:
            button.update()

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.fill((116, 143, 112))

        add_img = Assets.get_image("ui/plus.png", alpha=True)
        for button in self.buttons:
            button.draw(surf)
            pos = Assets.position_by_percent(add_img.get_size(), button.rect.size, (0.5, 0.5))
            pos = pos[0] + button.rect.left, pos[1] + button.rect.top
            surf.blit(add_img, pos)

        if self.selected:
            self.remove_button.draw(surf)

        self.back_button.draw(surf)
        self.next_button.draw(surf)

        return surf
