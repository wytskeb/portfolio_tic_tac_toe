class Board:
    def __init__(self, size_game):
        self.size_game = size_game
        self.board = [[" " for _ in range(size_game)] for _ in range(size_game)]
    
    def create_new_board(self, size):
        return [[" " for _ in range(size)] for _ in range(size)]

    def make_move(self, move, symbol):
        x, y = move
        self.board[x-1][y-1] = symbol

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def check_winner(self):
        for i in range(self.size_game):
            if self.board[i][0] != " " and all(self.board[i][j] == self.board[i][0] for j in range(self.size_game)):
                return self.board[i][0]
            if self.board[0][i] != " " and all(self.board[j][i] == self.board[0][i] for j in range(self.size_game)):
                return self.board[0][i]
        if self.board[0][0] != " " and all(self.board[i][i] == self.board[0][0] for i in range(self.size_game)):
            return self.board[0][0]
        if self.board[0][self.size_game-1] != " " and all(self.board[i][self.size_game-1-i] == self.board[0][self.size_game-1] for i in range(self.size_game)):
            return self.board[0][self.size_game-1]
        return None
    
    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True
    
    def check_possible_moves(self):
        possible_moves = []
        for i in range(self.size_game):
            for j in range(self.size_game):
                if self.board[i][j] == " ":
                    possible_moves.append((i+1, j+1))
        return possible_moves

    def print_board(self):
        print("X  -", end="")
        print("-" * 2 * self.size_game)
        for row in self.board:
            print("|  |", end="")
            print("|".join(row) + "|")
            print("|  -", end="")
            print("-" * 2 * self.size_game)
        print ("v/Y--------->")

    