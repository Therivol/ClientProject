import pygame as p

from clue.scene.Scene import Scene
from gui.element.Button import Button
from util.Assets import Assets
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class View(Scene):
    def __init__(self):
        super().__init__("VIEW")

        self.back_button = Button(p.Rect(400, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.cards = []

    def set_cards(self, cards_list):
        self.cards = cards_list

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("CARDS")

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)

        text = Assets.font_1.render("Back", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.back_button.rect.size, (0.5, 0.5),
                                                    base=self.back_button.rect.topleft)))

        x, y = 0, 32
        for i, card in enumerate(self.cards):
            x = (i % 3) * 256 + 128
            if i > 2:
                y = 354

            p.draw.rect(surf, (140, 160, 140), (x, y, 224, 288))

            text = Assets.font_1.render(card, True, (0, 0, 0))
            loc = Assets.position_by_percent(text.get_size(), (224, 288), (0.5, 0.5), base=(x, y))
            surf.blit(text, loc)

        return surf
