import json

from util.Assets import Assets
from util.GameInstance import GameInstance
from util.Globals import Globals
from util.Scenes import Scenes
from clue.scene.Scene import Scene

from gui.element.Button import Button

import pygame as p

from util.Window import Window


class Menu(Scene):
    def __init__(self):
        super().__init__("MENU")

        self.new_button = Button(p.Rect(Assets.position_by_percent((192, 64), Globals.resolution,
                                                                   (0.5, 0.45)), (192, 64)), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.resume_button = Button(p.Rect(Assets.position_by_percent((192, 64), Globals.resolution,
                                                                    (0.5, 0.57)), (192, 64)), (64, 43, 29), (89, 66, 41),
                                  idle_border=(174, 174, 174))

        self.quit_button = Button(p.Rect(Assets.position_by_percent((192, 64), Globals.resolution,
                                            (0.5, 0.69)), (192, 64)), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

    def update(self):
        if self.new_button.update():
            Scenes.get_scene("ADD PLAYERS").clear()
            Scenes.set_scene("ADD PLAYERS")

        if self.resume_button.update():
            Scenes.set_scene("BOARD")

        if self.quit_button.update():
            Window.should_close = True

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        img = Assets.get_image("ui/clue_logo.png", alpha=True)
        surf.blit(img, Assets.position_by_percent(img.get_size(), Globals.resolution, (0.5, 0.2)))

        self.new_button.draw(surf)
        self.resume_button.draw(surf)
        self.quit_button.draw(surf)

        return surf
