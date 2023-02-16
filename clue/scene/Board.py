import json
import random

from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from clue.scene.Scene import Scene
from clue.Player import Player
import pygame as p


class Board(Scene):
    def __init__(self):
        super().__init__("BOARD")
        self.board = [[]]
        self.TILE_SIZE = 0
        self.players = []

    def awake(self):
        with open("assets/board/board.json", "r") as file:
            self.board = json.load(file)

        self.TILE_SIZE = Settings.get("TILE SIZE")

        self.add_player(Player("Player 1", (5, 1), (255, 0, 0)))

    def update(self):
        if Input.get_key_down(p.K_SPACE):
            print(random.randint(1, 6))

        if Input.get_key_down(p.K_ESCAPE):
            Scenes.set_scene("MENU")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill((200, 200, 200))

        y = 0
        for row in self.board:
            x = 0
            for tile in row:
                color = (0, 0, 0)

                outline = (0, 0, 0)

                if tile == 0:
                    color = (0, 0, 0)
                elif tile == 1:
                    color = (200, 200, 200)
                elif tile == 2:
                    color = (209, 185, 128)
                    outline = (229, 205, 148)
                elif tile == 3:
                    color = (125, 150, 125)
                elif tile == 4:
                    color = (125, 125, 150)

                if tile != 1:
                    x_pos, y_pos = x * self.TILE_SIZE, y * self.TILE_SIZE
                    p.draw.rect(surf, color, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE))

                    p.draw.rect(surf, outline, (x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE), 1)
                x += 1
            y += 1

        self.draw_players(surf)

        return surf

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, name):
        self.players = [player for player in self.players if player.name != name]

    def draw_players(self, surf):
        for player in self.players:

            p.draw.rect(surf, (0, 0, 0), p.Rect(player.location * self.TILE_SIZE, (self.TILE_SIZE, self.TILE_SIZE)))
            p.draw.circle(surf, player.color, player.location * self.TILE_SIZE +
                          (self.TILE_SIZE / 2, self.TILE_SIZE / 2), self.TILE_SIZE / 2)
            p.draw.rect(surf, (0, 0, 0), p.Rect(player.location * self.TILE_SIZE, (self.TILE_SIZE, self.TILE_SIZE)), 2)

