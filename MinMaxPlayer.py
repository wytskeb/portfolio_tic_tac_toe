import math
import copy
#from random import choice


class MinMaxPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def minimax(self, board, depth, is_maximizing):
        if depth == 0 or board.check_draw() or board.check_winner():
            return self.evaluate_board(board)

        if is_maximizing:
            best_eval = float('-inf')
            for move in board.check_possible_moves():
                print(f"move: {move} symbol: {self.symbol} depth: {depth} is_maximizing: {is_maximizing}")
                cloned_board = copy.deepcopy(board)
                cloned_board.make_move(move, self.symbol)
                eval_score = self.minimax(cloned_board, depth - 1, False)
                best_eval = max(best_eval, eval_score)
            return best_eval
        else:
            best_eval = float('inf')
            for move in board.check_possible_moves():
                print(f"move: {move} symbol: {self.symbol} depth: {depth} is_maximizing: {is_maximizing}")
                cloned_board = copy.deepcopy(board)
                cloned_board.make_move(move, 'X' if self.symbol == 'O' else 'O')
                eval_score = self.minimax(cloned_board, depth - 1, True)
                best_eval = min(best_eval, eval_score)
            return best_eval

    def evaluate_board(self, board):
        if board.check_winner() == self.symbol:
            return 1
        elif board.check_winner() == ('X' if self.symbol == 'O' else 'O'):
            return -1
        else:
            return 0

    def get_move(self, board):
        best_move = -1
        best_eval = float('-inf')
        for move in board.check_possible_moves():
            cloned_board = copy.deepcopy(board)
            cloned_board.make_move(move, self.symbol)
            eval_score = self.minimax(cloned_board, 9, False)  # Depth 9 for Tic-Tac-Toe
            if eval_score > best_eval:
                best_eval = eval_score
                best_move = move
                print(f"Best move: {best_move} with score: {best_eval}")
        return best_move