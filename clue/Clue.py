import pygame as p

from util.Settings import Settings
from util.Window import Window
from util.Scenes import Scenes

from clue.scene.Board import Board
from clue.scene.Menu import Menu

from clue.Game import Game


class Clue(Game):
    def start(self):
        Window.display = p.display.set_mode(Settings.get("RESOLUTION"))
        p.display.set_caption(Settings.get("TITLE"))
        Window.resize(Settings.get("WINDOW SIZE"))

        Scenes.add_scene(Board())
        Scenes.add_scene(Menu())
        Scenes.set_scene("MENU")
