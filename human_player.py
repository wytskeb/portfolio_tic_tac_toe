"""Human player module"""
class HumanPlayer:
    """Human player class"""
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"{self.symbol}"

    def __str__(self):
        return f"{self.symbol}"
    def get_move(self, board):
        """Gets a move from the human player"""
        n = board.size_game
        print(f"Mogelijke zetten: {board.check_possible_moves()}")
        player_input = input("Geef een positie: ").split(',')
        if len(player_input) != 2:
            print("Ongeldige positie")
            return None, None
        try:
            x = int(player_input[0])
            y = int(player_input[1])
        except ValueError:
            print("Ongeldige positie")
            return None, None

        if 0 < x <= n and 0 < y <= n and (x, y) in board.check_possible_moves():
            return (x, y)
        print("Positie is niet beschikbaar")
        return None, None
