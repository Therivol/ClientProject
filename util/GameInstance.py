import json

from clue.Player import Player
from util.ClueUtil import ClueUtil


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
        board.accuse = []

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
        board.player_cards = save[6]

        player_cards = sum(save[6].values(), [])
        board.accuse = [card for card in ClueUtil.cards() if card not in player_cards]

        if not board.moved:
            board.set_moves()

    @staticmethod
    def save_instance(board):
        players = []

        for token in board.tokens:
            hashed = token.hash()
            players.append(hashed)

        save = [players, board.turn, board.die_roll, str(board.moved), str(True), board.players,
                board.player_cards]

        with open("assets/save/save.json", 'w') as file:
            json.dump(save, file)

    @staticmethod
    def new_instance():
        GameInstance.players = [None for _ in range(6)]
        GameInstance.started = False
