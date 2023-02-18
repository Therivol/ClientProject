import pygame as p
from gui.element.UIElement import UIElement
from util.Input import Input
from util.Assets import Assets


class Button(UIElement):
    def __init__(self, rect, idle_color, active_color, idle_border=None, active_border=None):
        super().__init__()
        self.rect = rect
        self.idle = idle_color
        self.active = active_color
        self.current_color = idle_color
        self.pressed = False
        self.border = idle_border
        self.idle_border = idle_border
        self.active_border = active_border

    def update(self):
        self.pressed = False
        if self.rect.collidepoint(Input.get_mouse_pos()):
            self.current_color = self.active
            self.border = self.active_border
            if Input.get_button_down(0):
                self.pressed = True
        else:
            self.current_color = self.idle
            self.border = self.idle_border

        return self.pressed

    def draw(self, surface):
        p.draw.rect(surface, self.current_color, self.rect)
        if self.border:
            p.draw.rect(surface, self.border, self.rect, 2)


class ButtonSurf(UIElement):
    def __init__(self, rect, idle_surf, active_surf):
        super().__init__()
        self.rect = rect
        self.idle = idle_surf
        self.active = active_surf
        self.current_surf = idle_surf
        self.pressed = False

    def update(self):
        self.pressed = False
        if self.rect.collidepoint(Input.get_mouse_pos()):
            self.current_surf = self.active
            if Input.get_button_down(0):
                self.pressed = True
        else:
            self.current_surf = self.idle

        return self.pressed

    def draw(self, surface):
        surface.blit(Assets.get_image(self.current_surf), self.rect.topleft)
