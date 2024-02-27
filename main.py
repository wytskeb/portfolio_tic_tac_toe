from random import randint

import Board

import HumanPlayer
#import RandomPlayer
import MinMaxPlayer

SIZE_GAME_MIN = 3
SIZE_GAME_MAX = 3
size_game = randint(SIZE_GAME_MIN, SIZE_GAME_MAX )

aantal_x = 0
aantal_o = 0
winning_human = 0
winning_computer = 0

def play_game(player_x, player_o):
    move = 0

    while True:
        if move % 2 == 0:
            player = player_x
            sine = "X"
        else:
            player = player_o
            sine = "O"

        print (f"Move: {move+1}")
        x, y = player.get_move(board)

        if x == None or y == None:
            print("Onjuist antwoord, probeer opnieuw!")
            continue

        print(x)
        print(y)

        board.make_move((x, y), sine)

        board.print_board()

        if board.check_winner() == sine:
            print("Speler 1 heeft gewonnen!")
            return sine
        if board.check_draw():
            print("Gelijkspel!")
            return None
        
        move += 1
        
while True:
    print(f"Het spel begint! We spelen op een {size_game} X {size_game} bord. Wie het eerst {size_game} op rij heeft!")

    board = Board.Board(size_game)
    board.print_board()

    print("Speler 1 is X, speler 2 is O")
    
    tos = randint(0, 1)
    if tos == 0:
        print("Speler 1 is Mens")
        player1 = HumanPlayer.HumanPlayer("X")
        player2 = MinMaxPlayer.MinMaxPlayer("O")
    else:
        print("Speler 1 is  Computer MinMax")
        player1 = MinMaxPlayer.MinMaxPlayer("X")
        player2 = HumanPlayer.HumanPlayer("O")

    gewonnen = play_game(player1, player2)
    if (gewonnen == "X"):
        print("Speler 1 heeft gewonnen!")
        aantal_x += 1
        if tos == 0:
            winning_human += 1
        elif tos == 1:
            winning_computer += 1
    elif (gewonnen == "O"):
        print("Speler 2 heeft gewonnen!")
        aantal_o += 1
        if tos == 0:
            winning_computer += 1
        elif tos == 1:
            winning_human += 1

    nog_een_keer = input (f"Het staat X/O: ({aantal_x} / {aantal_o}). \nmens ({winning_human} / computer {winning_computer}). Nog een keer? (j/n) ")
    
    size_game = randint(SIZE_GAME_MIN, SIZE_GAME_MAX )

    if (nog_een_keer == "j"):
        board = Board.Board(size_game)
    else:
        break
    
