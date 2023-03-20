import pygame as p

from clue.scene.Scene import Scene
from gui.element.Button import Button
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class Popup(Scene):
    def __init__(self):
        super().__init__("POPUP")

        self.shadow = None

        self.okay_button = Button(p.Rect(384, 300, 192, 64), (0, 0, 0), (50, 50, 50))

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.okay_button.update():
            Scenes.set_scene(Scenes.last_scene)

    def get_surface(self):
        surf = p.Surface(Globals.resolution)

        surf.blit(Scenes.get_surface(Scenes.last_scene), (0, 0))

        surf.blit(self.shadow, (334, 130))

        self.okay_button.draw(surf)

        return surf
