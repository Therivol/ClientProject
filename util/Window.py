import pygame as p
import sys

from util.Settings import Settings
from util.Scenes import Scenes


class Window:

    should_close = False
    display = None
    view = None
    view_destination = (0, 0)
    full_screen = False

    @staticmethod
    def monitor_size():
        return [p.display.Info().current_w, p.display.Info().current_h]

    @staticmethod
    def draw():

        Window.view.blit(p.transform.scale(Scenes.get_surface(), Window.view.get_size()), (0, 0))

        Window.display.blit(Window.view, Window.view_destination)

        p.display.update()

    @staticmethod
    def resize(size):
        aspect = Settings.get("ASPECT RATIO")
        if size[1] * aspect > size[0]:
            Window.view = p.Surface((size[0], size[0] / aspect))
        else:
            Window.view = p.Surface((size[1] * aspect, size[1]))

        Window.view_destination = (Window.display.get_width() / 2 - Window.view.get_width() / 2,
                                 Window.display.get_height() / 2 - Window.view.get_height() / 2)
