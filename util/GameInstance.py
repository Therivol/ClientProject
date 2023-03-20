import json

from clue.Player import Player


class GameInstance:
    players = [None for _ in range(6)]
    started = False
    game_turn = 0

    @staticmethod
    def load_instance():
        print("loading")

        GameInstance.started = True
        with open("assets/save/save.json", 'r') as file:
            save = json.load(file)

        GameInstance.game_turn = int(save[1])

        for i, hashed in enumerate(save[0]):
            if hashed == "":
                GameInstance.players[i] = None
            else:
                GameInstance.players[i] = Player(hashed=hashed)

    @staticmethod
    def save_instance():
        print("saving")
        players = []

        for player in GameInstance.players:
            hashed = ""
            if player is not None:
                hashed = player.hash()

            players.append(hashed)

        save = [players, GameInstance.game_turn]

        with open("assets/save/save.json", 'w') as file:
            json.dump(save, file)

    @staticmethod
    def new_instance():
        GameInstance.players = [None for _ in range(6)]
        GameInstance.started = False
