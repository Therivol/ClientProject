import pygame as p
from gui.element.UIElement import UIElement
from util.Input import Input
from util.Assets import Assets


class Select(UIElement):
    def __init__(self, rect, idle_color=None, active_color=None, idle_border=None, active_border=None, sensitive=False,
                 disable_color=None, disable_border=None):
        super().__init__()
        self.rect = rect
        self.idle = idle_color
        self.active = active_color
        self.pressed = False
        self.idle_border = idle_border
        self.active_border = active_border
        self.sensitive = sensitive
        self.disabled = False
        self.disable_color = disable_color
        self.disable_border = disable_border

    def set_disabled(self, disabled):
        self.disabled = disabled

    def toggle_disabled(self):
        self.disabled = not self.disabled

    def update(self):
        if self.disabled:
            return False

        if Input.get_button_down(0):
            if self.rect.collidepoint(Input.get_mouse_pos()):
                self.pressed = not self.pressed
            elif self.sensitive:
                self.pressed = False

        return self.pressed

    def draw(self, surface):
        if self.disabled:
            if self.disable_color:
                p.draw.rect(surface, self.disable_color, self.rect)
            if self.disable_border:
                p.draw.rect(surface, self.disable_border, self.rect, 2)

        elif self.pressed:
            if self.active:
                p.draw.rect(surface, self.active, self.rect)
            if self.active_border:
                p.draw.rect(surface, self.active_border, self.rect, 2)

        else:
            if self.idle:
                p.draw.rect(surface, self.idle, self.rect)
            if self.idle_border:
                p.draw.rect(surface, self.idle_border, self.rect, 2)
