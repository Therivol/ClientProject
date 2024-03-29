from util.Assets import Assets
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes
from clue.scene.Scene import Scene

from gui.element.Button import Button

import pygame as p

class Pause(Scene):
    def __init__(self):
        super().__init__("PAUSE")

        self.resume_button = Button(p.Rect(416, 272, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.info_button = Button(p.Rect(416, 368, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.quit_button = Button(p.Rect(416, 464, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.resume_button.update():
            Scenes.set_scene("BOARD")

        if self.info_button.update():
            Scenes.set_scene("CARDS")

        if self.quit_button.update():
            Scenes.set_scene("MENU")

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.resume_button.draw(surf)
        text = Assets.font_1.render("Resume", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.resume_button.rect.size, (0.5, 0.5),
                                                    base=self.resume_button.rect.topleft)))

        self.info_button.draw(surf)
        text = Assets.font_1.render("View Cards", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.info_button.rect.size, (0.5, 0.5),
                                                    base=self.info_button.rect.topleft)))

        self.quit_button.draw(surf)
        text = Assets.font_1.render("Menu", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.quit_button.rect.size, (0.5, 0.5),
                                                    base=self.quit_button.rect.topleft)))

        return surf
