import pygame as p

from util.Scenes import Scenes
from util.Globals import Globals
from util.Settings import Settings


class Window:
    should_close = False
    display = None
    view = None
    view_destination = (0, 0)
    full_screen = False

    @staticmethod
    def awake():
        Window.display = p.display.set_mode(Globals.resolution)
        p.display.set_caption(Settings.get("TITLE"))
        Window.resize(Globals.window_size)

    @staticmethod
    def draw():

        Window.view.blit(p.transform.scale(Scenes.get_surface(), Window.view.get_size()), (0, 0))

        Window.display.blit(Window.view, Window.view_destination)

        p.display.update()

    @staticmethod
    def toggle_full_screen():
        Window.full_screen = not Window.full_screen

        if Window.full_screen:
            Window.display = p.display.set_mode(Globals.monitor_size, p.FULLSCREEN)
            Window.resize(Globals.monitor_size)

        else:
            Window.display = p.display.set_mode(Globals.window_size)
            Window.resize(Globals.window_size)

    @staticmethod
    def resize(size):

        res = Globals.resolution
        aspect = res[0] / res[1]

        if size[1] * aspect > size[0]:
            Window.view = p.Surface((size[0], size[0] / aspect))
        else:
            Window.view = p.Surface((size[1] * aspect, size[1]))

        Window.view_destination = (Window.display.get_width() / 2 - Window.view.get_width() / 2,
                                   Window.display.get_height() / 2 - Window.view.get_height() / 2)
