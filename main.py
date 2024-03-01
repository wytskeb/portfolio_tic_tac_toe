"""Main module"""
import sys
from random import randint
from board import Board

import human_player
#import random_player
import mini_max_player

SIZE_GAME_MIN = 3
SIZE_GAME_MAX = 3

def play_game(player_x, player_o, my_size_game):
    """Plays a game"""
    move = 0
    myboard = Board(my_size_game)
    myboard.print_board()

    while True:
        if move % 2 == 0:
            player = player_x
            sine = "X"
        else:
            player = player_o
            sine = "O"

        print (f"Move: {move+1}")
        x, y = player.get_move(myboard)

        if x is None or y is None:
            print("Onjuist antwoord, probeer opnieuw!")
            continue

        print(x)
        print(y)

        myboard.make_move((x, y), sine)

        myboard.print_board()

        if myboard.check_winner() == sine:
            print("Speler 1 heeft gewonnen!")
            return sine
        if myboard.check_draw():
            print("Gelijkspel!")
            return None
        move += 1

if __name__ == "__main__":
    AANTAL_X = 0
    AANTAL_O = 0
    WINNING_HUMAN = 0
    WINNING_COMPUTER = 0

    while True:

        size_game = randint(SIZE_GAME_MIN, SIZE_GAME_MAX)

        print(f"Het spel begint! We spelen op een {size_game} X {size_game} bord.")
        print(f"Wie het eerst {size_game} op rij heeft!")
        print("Speler 1 is X, speler 2 is O")

        tos = randint(0, 1)
        if tos == 0:
            print("Speler 1 is Mens")
            player1 = human_player.HumanPlayer("X")
            player2 = mini_max_player.MinMaxPlayer("O")
        else:
            print("Speler 1 is Computer MinMax")
            player1 = mini_max_player.MinMaxPlayer("X")
            player2 = human_player.HumanPlayer("O")

        gewonnen = play_game(player1, player2, size_game)
        if gewonnen == "X":
            print("Speler 1 heeft gewonnen!")
            AANTAL_X += 1
            if tos == 0:
                WINNING_HUMAN += 1
            else:
                WINNING_COMPUTER += 1
        elif gewonnen == "O":
            print("Speler 2 heeft gewonnen!")
            AANTAL_O += 1
            if tos == 0:
                WINNING_COMPUTER += 1
            else:
                WINNING_HUMAN += 1
        else:
            print("Gelijkspel!")

        print(f"Het staat X/O: ({AANTAL_X} / {AANTAL_O}).")
        print(f"mens ({WINNING_HUMAN} / computer {WINNING_COMPUTER})")

        nog_een_keer = input (". Nog een keer? (j/n) ")
        if nog_een_keer == "n":
            sys.exit()
