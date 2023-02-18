import sys
from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Globals import Globals
from util.Window import Window
import pygame as p


class Game:
    def __init__(self):
        p.init()
        Time.awake()
        Settings.load()
        Globals.awake()
        Window.awake()

        self.should_close = False

    def start(self):
        pass

    def poll_events(self):

        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT or Window.should_close:
                self.should_close = True

            if ev.type == p.VIDEORESIZE:
                Window.resize((ev.w, ev.h))

        if Input.get_key_down(p.K_F11):
            Window.toggle_full_screen()

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
