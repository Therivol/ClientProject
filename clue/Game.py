import sys
from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets
from util.Window import Window
import pygame as p


class Game:
    def __init__(self):
        p.init()
        Time.awake()
        Settings.load()

        self.should_close = False

    def start(self):
        pass

    def poll_events(self):

        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT or Window.should_close:
                self.should_close = True

            # if ev.type == p.VIDEORESIZE:
                # Window.resize((ev.w, ev.h))

        # if Input.get_key_down(p.K_F11):
            # Window.full_screen = not Window.full_screen
            # if Window.full_screen:
                # Window.display = p.display.set_mode(Window.monitor_size(), p.FULLSCREEN)
                # Window.resize(Window.monitor_size())
            # else:
                # Window.display = p.display.set_mode(Settings.get("WINDOW SIZE"), p.RESIZABLE)

    @staticmethod
    def start_frame():
        Time.start_frame()

    @staticmethod
    def calculate_dt():
        Time.calculate_dt()

    def update(self):
        Scenes.update()

    def draw(self):
        Window.draw()

    def quit(self):
        Settings.save()

        self.should_close = True
        p.quit()
        sys.exit()
