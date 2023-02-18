import pygame as p

from pygame.math import Vector2


class Player:
    def __init__(self, name, location, color, token, room=""):
        self.token = token
        self.name = name
        self.location = p.Vector2(location)
        self.color = color
        self.room = room

    def set_location(self, location):
        self.location.update(location)

    def set_color(self, color):
        self.color = color

    def set_room(self, room):
        self.room = room
