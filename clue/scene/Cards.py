import pygame as p

from clue.scene.Scene import Scene
from gui.element.Button import Button
from util.Assets import Assets
from util.Globals import Globals
from util.Input import Input
from util.Scenes import Scenes


class Cards(Scene):
    def __init__(self):
        super().__init__("CARDS")

        self.back_button = Button(p.Rect(416, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.view_button = Button(p.Rect(416, 352, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.accuse_button = Button(p.Rect(416, 448, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.left_button = Button(p.Rect(224, 64, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.right_button = Button(p.Rect(672, 64, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.token_select = 0
        self.players = []
        self.room = ""

    def set_room(self, room):
        self.room = room

    def enter(self):
        self.token_select = 0
        self.players = Scenes.get_scene("BOARD").players

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("PAUSE")

        if self.view_button.update():
            Scenes.set_scene("VIEW")
            Scenes.get_scene("VIEW").set_cards(
                Scenes.get_scene("BOARD").player_cards[str(self.players[self.token_select])])

        if self.accuse_button.update():
            Scenes.set_scene("VIEW")
            Scenes.get_scene("VIEW").set_cards(Scenes.get_scene("BOARD").accuse)

        if self.right_button.update() or Input.get_key_down(p.K_RIGHT):
            self.token_select += 1
            if self.token_select > len(self.players) - 1:
                self.token_select = 0

        if self.left_button.update() or Input.get_key_down(p.K_LEFT):
            self.token_select -= 1
            if self.token_select < 0:
                self.token_select = len(self.players) - 1

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)
        text = Assets.font_1.render("Back", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.back_button.rect.size, (0.5, 0.5),
                                                    base=self.back_button.rect.topleft)))

        self.left_button.draw(surf)
        text = Assets.font_1.render("<", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.left_button.rect.size, (0.5, 0.5),
                                                    base=self.left_button.rect.topleft)))

        self.right_button.draw(surf)
        text = Assets.font_1.render(">", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.right_button.rect.size, (0.5, 0.5),
                                                    base=self.right_button.rect.topleft)))

        self.view_button.draw(surf)
        text = Assets.font_1.render("View Cards", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.view_button.rect.size, (0.5, 0.5),
                                                    base=self.view_button.rect.topleft)))

        self.accuse_button.draw(surf)
        text = Assets.font_1.render("Accused", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.accuse_button.rect.size, (0.5, 0.5),
                                                    base=self.accuse_button.rect.topleft)))

        token = Scenes.get_scene("BOARD").tokens[self.players[self.token_select]].token
        surf.blit(p.transform.scale(Assets.get_image(f"tokens/{token}.png", True), (192, 192)),
                (416, 64))

        return surf
