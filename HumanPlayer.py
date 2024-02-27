class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol
        
    def get_move(self, board):
        n = board.size_game
        print(f"Mogelijke zetten: {board.check_possible_moves()}")
        player_input = input("Geef een positie: ").split(',')
        if len(player_input) != 2:
            print("Ongeldige positie")
            return None, None
        else:
            try:
                x = int(player_input[0])
                y = int(player_input[1])
            except ValueError:
                print("Ongeldige positie")
                return None, None
            else:

                if 0 < x <= n and 0 < y <= n and (x, y) in board.check_possible_moves():
                    return (x, y)
                
                print("Positie is niet beschikbaar")
                return None, None
