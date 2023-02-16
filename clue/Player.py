import pygame as p


class Player:
    def __init__(self):
        self.location = (0, 0)
        self.color = (0, 0, 0)
        self.room = ""

    def set_location(self, location):
        self.location = location

    def set_color(self, color):
        self.color = color

    def set_room(self, room):
        self.room = room
