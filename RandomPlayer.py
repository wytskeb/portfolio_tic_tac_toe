from random import choice

class RandomPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self,board):
        print(board.check_possible_moves())
        given_row, given_col = choice(board.check_possible_moves())
        print(given_row, given_col)
        return given_row, given_col
