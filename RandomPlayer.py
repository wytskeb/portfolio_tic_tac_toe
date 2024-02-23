from random import choice

class RandomPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self,n, possible_moves):
        print(n)
        given_row, given_col = choice(possible_moves)
        print(given_row, given_col)
        return given_row, given_col
