import json

from clue.Player import Player


class GameInstance:
    players = [None for _ in range(6)]
    started = True

    @staticmethod
    def load_instance(board):

        GameInstance.started = True
        with open("assets/save/save.json", 'r') as file:
            save = json.load(file)

        board.turn = save[1]
        board.die_roll = save[2]
        board.moved = bool(save[3])
        board.can_guess = bool(save[4])
        board.roll_button.set_disabled(board.die_roll != 0)
        board.players = []
        board.tokens = []

        for i, hashed in enumerate(save[0]):
            player = Player(hashed=hashed)
            board.tokens.append(player)
            if player.player:
                try:
                    GameInstance.players[i] = player
                except IndexError:
                    print(GameInstance.players, i)
            else:
                GameInstance.players[i] = None

        board.players = save[5]

        if not board.moved:
            board.set_moves()

    @staticmethod
    def save_instance(board):
        players = []

        for token in board.tokens:
            hashed = token.hash()
            players.append(hashed)

        save = [players, board.turn, board.die_roll, str(board.moved), str(board.can_guess), board.players]

        with open("assets/save/save.json", 'w') as file:
            json.dump(save, file)

    @staticmethod
    def new_instance():
        GameInstance.players = [None for _ in range(6)]
        GameInstance.started = False
