"""MinMaxPlayer.py"""
import copy
#from random import choice


class MinMaxPlayer:
    """MinMaxPlayer class"""
    def __init__(self, symbol):
        self.symbol = symbol

    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm"""
        if depth == 0 or board.check_draw() or board.check_winner():
            return self.evaluate_board(board)

        if is_maximizing:
            best_eval = float('-inf')
            for move in board.check_possible_moves():
                print(f"move: {move} symbol: {self.symbol}")
                print(f"depth: {depth} is_maximizing: {is_maximizing}")
                cloned_board = copy.deepcopy(board)
                cloned_board.make_move(move, self.symbol)
                eval_score = self.minimax(cloned_board, depth - 1, False)
                best_eval = max(best_eval, eval_score)
            return best_eval
        best_eval = float('inf')
        for move in board.check_possible_moves():
            print(f"move: {move} symbol: {self.symbol}")
            print(f"depth: {depth} is_maximizing: {is_maximizing}")
            cloned_board = copy.deepcopy(board)
            cloned_board.make_move(move, 'X' if self.symbol == 'O' else 'O')
            eval_score = self.minimax(cloned_board, depth - 1, True)
            best_eval = min(best_eval, eval_score)
        return best_eval

    def evaluate_board(self, board):
        """Evaluates the board"""
        if board.check_winner() == self.symbol:
            return 1
        if board.check_winner() == ('X' if self.symbol == 'O' else 'O'):
            return -1
        return 0

    def get_move(self, board):
        """Gets a move from the min max player"""
        best_move = -1
        best_eval = float('-inf')
        for move in board.check_possible_moves():
            cloned_board = copy.deepcopy(board)
            cloned_board.make_move(move, self.symbol)
            eval_score = self.minimax(cloned_board, 5, False)  # Depth 9 for Tic-Tac-Toe
            if eval_score > best_eval:
                best_eval = eval_score
                best_move = move
                print(f"Best move: {best_move} with score: {best_eval}")
        return best_move
    