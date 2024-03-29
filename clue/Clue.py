import pygame as p

from clue.scene.Cards import Cards
from clue.scene.Guess import Guess
from clue.scene.View import View
from util.Assets import Assets
from util.Scenes import Scenes

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
        Scenes.add_scene(Guess())
        Scenes.add_scene(Cards())
        Scenes.add_scene(View())
        Scenes.set_scene("MENU")

        p.display.set_icon(Assets.get_image("dice/1.png"))
