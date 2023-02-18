import pygame as p

from util.Settings import Settings


class Globals:

    monitor_size = [0, 0]
    resolution = [0, 0]
    window_size = [0, 0]
    game_instance = None

    @staticmethod
    def awake():
        Globals.set_monitor_size([p.display.Info().current_w, p.display.Info().current_h])
        Globals.set_resolution(Settings.get("RESOLUTION"))
        Globals.set_window_size(Settings.get("WINDOW SIZE"))

    @staticmethod
    def set_monitor_size(monitor_size):
        Globals.monitor_size = monitor_size

    @staticmethod
    def set_resolution(resolution):
        Globals.resolution = resolution

    @staticmethod
    def set_window_size(window_size):
        Globals.window_size = window_size

    @staticmethod
    def set_game_instance(instance):
        Globals.game_instance = instance
