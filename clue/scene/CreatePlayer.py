import pygame as p

from clue.Player import Player
from clue.scene.Scene import Scene
from gui.element.Button import Button
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

        self.left_button = Button(p.Rect(224, 128, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.right_button = Button(p.Rect(672, 128, 128, 192), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.token_select = 0
        self.tokens = []
        self.player = None

    def enter(self):
        self.token_select = 0
        players = Scenes.get_scene("ADD PLAYERS").players

        self.tokens = ClueUtil.characters()
        for player in players:
            if player and player.token in self.tokens:
                self.tokens.remove(player.token)

        self.next_button.set_disabled(True)
        self.player = Player("1", (0, 0), "MISS SCARLET")

    def awake(self):
        self.shadow = p.Surface((292, 284))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(150)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("ADD PLAYERS")

        if self.next_button.update() or Input.get_key_down(p.K_RETURN):
            self.player.token = self.tokens[self.token_select]
            Scenes.set_scene("ADD PLAYERS")
            Scenes.get_scene("ADD PLAYERS").add_player(self.player)

        if self.right_button.update() or Input.get_key_down(p.K_RIGHT):
            self.token_select += 1
            if self.token_select > len(self.tokens) - 1:
                self.token_select = 0

        if self.left_button.update() or Input.get_key_down(p.K_LEFT):
            self.token_select -= 1
            if self.token_select < 0:
                self.token_select = len(self.tokens) - 1

        self.next_button.set_disabled(self.token_select is None)

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.blit(Assets.get_image("ui/background.png"), (0, 0))

        self.back_button.draw(surf)
        text = Assets.font_1.render("Back", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.back_button.rect.size, (0.5, 0.5),
                                                    base=self.back_button.rect.topleft)))

        self.next_button.draw(surf)
        text = Assets.font_1.render("Confirm", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.next_button.rect.size, (0.5, 0.5),
                                                    base=self.next_button.rect.topleft)))

        self.left_button.draw(surf)
        text = Assets.font_1.render("<", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.left_button.rect.size, (0.5, 0.5),
                                                    base=self.left_button.rect.topleft)))

        self.right_button.draw(surf)
        text = Assets.font_1.render(">", True, (255, 255, 255))
        surf.blit(text, (Assets.position_by_percent(text.get_size(), self.right_button.rect.size, (0.5, 0.5),
                                                    base=self.right_button.rect.topleft)))

        surf.blit(p.transform.scale(Assets.get_image(f"tokens/{self.tokens[self.token_select]}.png", True), (192, 192)),
                (416, 128))

        return surf
