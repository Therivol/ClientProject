import json

from util.Assets import Assets
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes
from clue.scene.Scene import Scene

from gui.element.Button import Button

import pygame as p

from util.Window import Window


class Menu(Scene):
    def __init__(self):
        super().__init__("MENU")

        self.play_button = Button(p.Rect(Assets.position_by_percent((192, 64), Globals.resolution,
                                            (0.5, 0.5)), (192, 64)), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.quit_button = Button(p.Rect(Assets.position_by_percent((192, 64), Globals.resolution,
                                            (0.5, 0.65)), (192, 64)), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

    def update(self):
        if self.play_button.update():
            Scenes.set_scene("ADD PLAYERS")

        if self.quit_button.update():
            Window.should_close = True

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.fill((116, 143, 112))

        img = Assets.get_image("ui/clue_logo.png", alpha=True)
        surf.blit(img, Assets.position_by_percent(img.get_size(), Globals.resolution, (0.5, 0.2)))

        self.play_button.draw(surf)
        self.quit_button.draw(surf)

        return surf
