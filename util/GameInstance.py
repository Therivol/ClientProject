import json

from clue.Player import Player


class GameInstance:
    players = [None for _ in range(6)]
    started = False

    @staticmethod
    def load_instance(board):
        print("loading")

        GameInstance.started = True
        with open("assets/save/save.json", 'r') as file:
            save = json.load(file)

        board.turn = save[1]
        board.die_roll = save[2]
        board.moved = bool(save[3])
        board.can_guess = bool(save[4])
        board.roll_button.set_disabled(board.die_roll != 0)

        for i, hashed in enumerate(save[0]):
            GameInstance.players[i] = None if hashed == "" else Player(hashed=hashed)

        board.players = [player for player in GameInstance.players if player]

        if not board.moved:
            board.set_moves()

    @staticmethod
    def save_instance(board):
        print("saving")
        players = []

        for player in board.players:
            hashed = player.hash()
            players.append(hashed)

        save = [players, board.turn, board.die_roll, str(board.moved), str(board.can_guess)]

        with open("assets/save/save.json", 'w') as file:
            json.dump(save, file)

    @staticmethod
    def new_instance():
        GameInstance.players = [None for _ in range(6)]
        GameInstance.started = False
