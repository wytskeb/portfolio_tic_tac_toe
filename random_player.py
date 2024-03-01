"""RandomPlayer.py"""
from random import choice

class RandomPlayer:
    """RandomPlayer class"""
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"RandomPlayer({self.symbol})"

    def __str__(self):
        return f"RandomPlayer({self.symbol})"

    def get_move(self,board):
        """Gets a move from the random player"""
        print(board.check_possible_moves())
        given_row, given_col = choice(board.check_possible_moves())
        print(given_row, given_col)
        return given_row, given_col
