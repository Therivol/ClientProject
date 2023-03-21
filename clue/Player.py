import pygame as p

from pygame.math import Vector2


class Player:
    def __init__(self, name="", location=(0, 0), token="MISS SCARLET", room="", player=True, hashed=None):
        self.token = token
        self.name = name
        self.location = p.Vector2(location)
        self.room = room
        self.player = player

        if hashed:
            self.load_hash(hashed)

    def set_location(self, location):
        self.location.update(location)

    def set_room(self, room):
        self.room = room

    def hash(self):
        return f"{self.player}~{self.token}~{self.name}~{self.location.x}~{self.location.y}~{self.room}"

    def load_hash(self, hash):
        values = hash.split('~')
        self.player = values[0]
        self.token = values[1]
        self.name = values[2]
        self.location = p.Vector2(float(values[3]), float(values[4]))
        self.room = values[5]
