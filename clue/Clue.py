import pygame as p

from util.Settings import Settings
from util.Window import Window
from util.Scenes import Scenes
from util.Globals import Globals

from clue.scene.Board import Board
from clue.scene.Menu import Menu
from clue.scene.Popup import Popup
from clue.scene.AddPlayers import AddPlayers
from clue.scene.CreatePlayer import CreatePlayer
from clue.scene.Pause import Pause
from clue.Game import Game


class Clue(Game):
    def start(self):

        Scenes.add_scene(Board())
        Scenes.add_scene(AddPlayers())
        Scenes.add_scene(Menu())
        Scenes.add_scene(Popup())
        Scenes.add_scene(CreatePlayer())
        Scenes.add_scene(Pause())
        Scenes.set_scene("MENU")
