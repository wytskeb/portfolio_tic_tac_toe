"""Board module"""
class Board:
    """Board class"""
    def __init__(self, size_game):
        """Creates a new board"""
        self.size_game = size_game
        self.board_class = [[" " for _ in range(size_game)] for _ in range(size_game)]
    def create_new_board(self, size):
        """Creates a new board"""
        return [[" " for _ in range(size)] for _ in range(size)]

    def make_move(self, move, symbol):
        """Makes a move on the board"""
        x, y = move
        self.board_class[x-1][y-1] = symbol

    def check_winner(self):
        """Returns the winner or None if there is no winner"""
        for i in range(self.size_game):
            if (self.board_class[i][0] != " " and
                all(self.board_class[i][j] == self.board_class[i][0]
                    for j in range(self.size_game))):
                return self.board_class[i][0]
            if (self.board_class[0][i] != " " and
                all(self.board_class[j][i] == self.board_class[0][i]
                    for j in range(self.size_game))):
                return self.board_class[0][i]
        if (self.board_class[0][0] != " " and
            all(self.board_class[i][i] == self.board_class[0][0]
                for i in range(self.size_game))):
            return self.board_class[0][0]
        if (self.board_class[0][self.size_game-1] != " "and
            all(self.board_class[i][self.size_game-1-i] == self.board_class[0][self.size_game-1]
                for i in range(self.size_game))):
            return self.board_class[0][self.size_game-1]
        return None

    def check_draw(self):
        """Returns True if the board is full and no winner is found"""
        for row in self.board_class:
            if " " in row:
                return False
        return True

    def check_possible_moves(self):
        """Returns a list of possible moves"""
        possible_moves = []
        for i in range(self.size_game):
            for j in range(self.size_game):
                if self.board_class[i][j] == " ":
                    possible_moves.append((i+1, j+1))
        return possible_moves

    def print_board(self):
        """Prints the board to the console"""
        print("X  -", end="")
        print("-" * 2 * self.size_game)
        for row in self.board_class:
            print("|  |", end="")
            print("|".join(row) + "|")
            print("|  -", end="")
            print("-" * 2 * self.size_game)
        print ("v/Y--------->")
    