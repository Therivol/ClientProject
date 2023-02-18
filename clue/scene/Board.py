import json
import random

from gui.element.Button import Button
from util.Assets import Assets
from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Globals import Globals
from util.Time import Time
from clue.scene.Scene import Scene
from clue.Player import Player
import pygame as p
import pygame.gfxdraw


class Board(Scene):
    def __init__(self):
        super().__init__("BOARD")
        self.board = [[]]
        self.TILE_SIZE = 0
        self.players = []
        self.rolling = False
        self.roll_start = 0
        self.die_roll = 0

        self.roll_button = Button(p.Rect(800, 192, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.quit_button = Button(p.Rect(800, 672, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

    def awake(self):
        with open("assets/board/board.json", "r") as file:
            self.board = json.load(file)

        self.TILE_SIZE = Settings.get("TILE SIZE")

        self.add_player(Player("Player 1", (8, 3), (255, 0, 0), "MISS SCARLET"))
        self.add_player(Player("Player 1", (8, 4), (255, 0, 0), "MRS WHITE"))
        self.add_player(Player("Player 1", (8, 5), (255, 0, 0), "MRS PEACOCK"))
        self.add_player(Player("Player 1", (8, 6), (255, 0, 0), "PROFESSOR PLUM"))
        self.add_player(Player("Player 1", (8, 7), (255, 0, 0), "MR GREEN"))
        self.add_player(Player("Player 1", (8, 8), (255, 0, 0), "COLONEL MUSTARD"))

    def resize(self, size):
        aspect = 24 / 25

        if size[1] * aspect > size[0]:
            self.TILE_SIZE = int(size[0] / 24)
        else:
            self.TILE_SIZE = int(size[1] / 25)

    def update(self):
        if self.roll_button.update():
            self.roll_die()

        if self.quit_button.update():
            Scenes.set_scene("MENU")

        if self.rolling:
            if Time.time_s() - self.roll_start > 0.5:
                self.rolling = False
                self.die_roll = random.randint(1, 6)

        if Input.get_key_down(p.K_ESCAPE):
            Scenes.set_scene("MENU")

    def roll_die(self):
        if not self.rolling:
            self.roll_start = Time.time_s()
            self.die_roll = 0
            self.rolling = True

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.fill((116, 143, 112))
        self.draw_board(surf)
        self.draw_players(surf)
        self.draw_dice(surf)
        self.roll_button.draw(surf)
        self.quit_button.draw(surf)

        return surf

    def draw_dice(self, surf):
        surf.blit(Assets.get_image(f"dice/{self.die_roll}.png"), (832, 32))

    def draw_board(self, surf):
        surf.blit(Assets.get_image("board/board.png"), (0, 0))

    def draw_board_old(self, surf):
        y = 0
        for row in self.board:
            x = 0
            for tile in row:
                color = (0, 0, 0)

                outline = (0, 0, 0)

                if tile == 0:
                    color = (75, 90, 75)
                elif tile == 1:
                    color = (125, 96, 70)
                elif tile == 2:
                    color = (209, 185, 128)
                    outline = (229, 205, 148)
                elif tile == 3:
                    color = (125, 150, 125)
                elif tile == 4:
                    color = (125, 125, 150)

                x_pos, y_pos = x * self.TILE_SIZE, y * self.TILE_SIZE
                if tile == 2:
                    p.draw.rect(surf, color, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE))
                    p.draw.rect(surf, outline, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE), 1)
                else:
                    p.draw.rect(surf, color, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE))
                x += 1
            y += 1

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, name):
        self.players = [player for player in self.players if player.name != name]

    def draw_players(self, surf):
        for player in self.players:
            surf.blit(Assets.get_image(f"tokens/{player.token}.png", alpha=True), player.location * self.TILE_SIZE)
