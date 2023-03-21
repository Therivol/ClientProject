import json
import random

from clue.Player import Player
from gui.element.Button import Button
from util.Assets import Assets
from util.ClueUtil import ClueUtil
from util.GameInstance import GameInstance
from util.Settings import Settings
from util.Input import Input
from util.Scenes import Scenes
from util.Globals import Globals
from util.Time import Time
from clue.scene.Scene import Scene
import pygame as p


class Board(Scene):
    def __init__(self):
        super().__init__("BOARD")
        self.board = [[]]
        self.TILE_SIZE = 0
        self.tokens = []
        self.players = []
        self.player_cards = {}
        self.accuse = []
        self.rolling = False
        self.roll_start = 0
        self.die_roll = 0

        self.moved = False

        self.turn = 0
        self.start_positions = [(0, 18), (0, 5), (16, 0), (23, 7), (14, 24), (9, 24)]

        self.roll_button = Button(p.Rect(800, 352, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174),
                                  disable_color=(0, 0, 0))
        self.guess_button = Button(p.Rect(800, 480, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.options_button = Button(p.Rect(800, 576, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))
        self.end_button = Button(p.Rect(800, 704, 192, 64), (64, 43, 29), (89, 66, 41), idle_border=(174, 174, 174))

        self.available_moves = []

    def enter(self):
        if GameInstance.started:
            GameInstance.load_instance(self)

        else:
            self.start_board()

    def exit(self):
        GameInstance.save_instance(self)

    def start_board(self):
        self.tokens = []

        player_tokens = {player.token: player for player in GameInstance.players if player}
        for token in ClueUtil.characters():
            if token in player_tokens:
                self.tokens.append(player_tokens[token])
            else:
                self.tokens.append(Player(token=token, player=False))

        self.players = [self.tokens.index(player_tokens[token]) for token in player_tokens]

        self.accuse.append(ClueUtil.weapons()[random.randint(0, 5)])
        self.accuse.append(ClueUtil.characters()[random.randint(0, 5)])
        self.accuse.append(ClueUtil.rooms()[random.randint(0, 8)])

        self.player_cards = {index: [] for index in self.players}

        cards = ClueUtil.cards()
        random.shuffle(cards)
        player_counter = 0
        for card in cards:
            if card not in self.accuse:
                self.player_cards[self.players[player_counter]].append(card)
                player_counter = (player_counter + 1) % len(self.players)

        print(self.accuse, self.player_cards)

        self.turn = 0
        self.die_roll = 0
        self.moved = False

        i = 0
        for token in self.tokens:
            try:
                new_pos = self.start_positions[i]
            except IndexError:
                print(i, self.start_positions)
            i += 1

            token.set_location(new_pos)

        GameInstance.started = True

    def next_turn(self):

        self.turn = (self.turn + 1) % len(self.players)
        self.roll_button.set_disabled(False)
        self.die_roll = 0
        self.available_moves.clear()

        GameInstance.game_turn = self.turn

    def set_moves(self):
        self.available_moves.clear()

        moves = []

        player = self.tokens[self.players[self.turn]]

        if player.room != "":
            if player.room in ClueUtil.tunnels:
                self.add_move(p.Vector2(ClueUtil.tunnels[player.room]))

            for pos in ClueUtil.door_rooms[player.room]:
                moves += self.explore_pos(pos, self.die_roll)

            for move in moves:
                if move not in ClueUtil.door_rooms[player.room]:
                    self.add_move(move)

        else:
            pos = player.location
            moves += self.explore_pos(pos, self.die_roll)

            for move in moves:
                self.add_move(move)

    def explore_pos(self, pos, depth):
        if depth <= 0:
            return []

        discovered = []
        directions = [p.Vector2(0, -1), p.Vector2(1, 0), p.Vector2(0, 1), p.Vector2(-1, 0)]
        player_pos = [token.location for token in self.tokens if token.room == ""]
        for direction in directions:
            new_pos = pos + direction
            try:
                tile = self.board[int(new_pos.y)][int(new_pos.x)]
            except IndexError:
                continue
            if tile in [2, 3] and new_pos not in player_pos:
                discovered.append(new_pos)

        new_discovered = []
        for move in discovered:
            new_discovered += self.explore_pos(move, depth - 1)

        discovered += new_discovered
        return discovered

    def awake(self):
        with open("assets/board/board.json", "r") as file:
            self.board = json.load(file)

        self.TILE_SIZE = Settings.get("TILE SIZE")

    def resize(self, size):
        aspect = 24 / 25

        if size[1] * aspect > size[0]:
            self.TILE_SIZE = int(size[0] / 24)
        else:
            self.TILE_SIZE = int(size[1] / 25)

    def update(self):
        if self.roll_button.update():
            self.roll_die()

        if  self.guess_button.update() and self.tokens[self.players[self.turn]].room != "":
            Scenes.get_scene("GUESS").set_room(self.tokens[self.players[self.turn]].room)
            Scenes.set_scene("GUESS")

        if self.end_button.update():
            self.next_turn()

        if self.rolling and Time.time_s() - self.roll_start > 0.5:
            self.rolling = False
            self.die_roll = random.randint(1, 6)
            GameInstance.die_roll = self.die_roll
            self.set_moves()

        if Input.get_key_down(p.K_ESCAPE) or self.options_button.update():
            Scenes.set_scene("PAUSE")

        if Input.get_button_down(0):
            mouse_pos = Input.get_mouse_pos()
            x = int(mouse_pos[0] / self.TILE_SIZE)
            y = int(mouse_pos[1] / self.TILE_SIZE)

            if (x, y) in self.available_moves:
                self.move_player(p.Vector2(x, y))

    def move_player(self, pos):
        self.moved = True

        player = self.tokens[self.players[self.turn]]
        pos_xy = (pos.x, pos.y)
        if pos_xy in ClueUtil.room_doors:
            self.add_to_room(ClueUtil.room_doors[pos_xy], player.token)

        elif pos_xy in ClueUtil.tunnels_2:
            self.add_to_room(ClueUtil.tunnels_2[pos_xy], player.token)

        else:
            player.room = ""
            player.set_location(pos)

        self.available_moves.clear()

    def add_to_room(self, room, character):

        to_add = None
        for token in self.tokens:
            if token.token == character:
                to_add = token

        print(to_add)
        to_add.set_room(room)

        other_positions = [token.location for token in self.tokens]
        o_pos = ClueUtil.room_centers[room]
        pos = o_pos
        while pos in other_positions:
            pos = (random.randint(o_pos[0] - 1, o_pos[0] + 1), random.randint(o_pos[1], o_pos[1] + 1))

        to_add.set_location(pos)

    def roll_die(self):
        self.roll_button.set_disabled(True)
        if not self.rolling:
            self.roll_start = Time.time_s()
            self.die_roll = 0
            self.rolling = True

    def get_surface(self):
        surf = p.Surface(Globals.resolution)
        surf.fill((116, 143, 112))
        self.draw_board(surf)
        self.draw_tokens(surf)
        self.draw_moves(surf)
        self.draw_sidebar(surf)

        return surf

    def draw_sidebar(self, surf):
        surf.blit(p.transform.scale(Assets.get_image(f"tokens/{self.tokens[self.players[self.turn]].token}.png"),
                                    (128, 128)), (832, 32))

        surf.blit(Assets.get_image(f"dice/{self.die_roll}.png"), (832, 192))

        self.roll_button.draw(surf)
        self.guess_button.draw(surf)
        self.options_button.draw(surf)
        self.end_button.draw(surf)

    def draw_board(self, surf):
        surf.blit(Assets.get_image("board/board.png"), (0, 0))

    def draw_tokens(self, surf):
        for token in self.tokens:
            surf.blit(Assets.get_image(f"tokens/{token.token}.png", alpha=True), token.location * self.TILE_SIZE)

    def draw_moves(self, surf):
        test = p.Surface((self.TILE_SIZE, self.TILE_SIZE))
        test.fill((200, 255, 200))
        test.set_alpha(100)
        for pos in self.available_moves:
            surf.blit(test, pos * self.TILE_SIZE)

    def add_move(self, pos):
        if pos not in self.available_moves:
            self.available_moves.append(pos)
