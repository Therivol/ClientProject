import pygame as p
from gui.element.UIElement import UIElement
from util.Input import Input
from util.Assets import Assets


class Select(UIElement):
    def __init__(self, rect, idle_color, active_color, idle_border=None, active_border=None, sensitive=False):
        super().__init__()
        self.rect = rect
        self.idle = idle_color
        self.active = active_color
        self.pressed = False
        self.idle_border = idle_border
        self.active_border = active_border
        self.sensitive = sensitive

    def update(self):
        if Input.get_button_down(0):
            if self.rect.collidepoint(Input.get_mouse_pos()):
                self.pressed = not self.pressed
            elif self.sensitive:
                self.pressed = False

        return self.pressed

    def draw(self, surface):
        if self.pressed:
            p.draw.rect(surface, self.active, self.rect)
            if self.active_border:
                p.draw.rect(surface, self.active_border, self.rect, 2)

        else:
            p.draw.rect(surface, self.idle, self.rect)
            if self.idle_border:
                p.draw.rect(surface, self.idle_border, self.rect, 2)
