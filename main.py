from random import randint

import HumanPlayer
import RandomPlayer

size_game = randint(3, 6)

aantal_x = 0
aantal_o = 0
winning_human = 0
winning_computer = 0

board = [[" " for _ in range(size_game)] for _ in range(size_game)]

def print_board(board):
    print("X  -", end="")
    print("-" * 2 * size_game)
    for row in board:
        print("|  |", end="")
        print("|".join(row) + "|")
        print("|  -", end="")
        print("-" * 2 * size_game)
    print ("v/Y--------->")

def create_new_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


def check_winner(board):
    for i in range(size_game):
        if board[i][0] != " " and all(board[i][j] == board[i][0] for j in range(size_game)):
            return board[i][0]
        if board[0][i] != " " and all(board[j][i] == board[0][i] for j in range(size_game)):
            return board[0][i]
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(size_game)):
        return board[0][0]
    if board[0][size_game-1] != " " and all(board[i][size_game-1-i] == board[0][size_game-1] for i in range(size_game)):
        return board[0][size_game-1]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def check_possible_moves(board):
    possible_moves = []
    for i in range(size_game):
        for j in range(size_game):
            if board[i][j] == " ":
                possible_moves.append((i+1, j+1))
    return possible_moves

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
        x, y = player.get_move(size_game, check_possible_moves(board))

        if x == None or y == None:
            print("Onjuist antwoord, probeer opnieuw!")
            continue

        print(x)
        print(y)

        board[x-1][y-1] = sine

        print_board(board)

        if check_winner(board) == sine:
            print("Speler 1 heeft gewonnen!")
            return sine
        if check_draw(board):
            print("Gelijkspel!")
            return None
        
        move += 1
        
while True:
    print(f"Het spel begint! We spelen op een {size_game} X {size_game} bord. Wie het eerst {size_game} op rij heeft!")
    print_board(board)

    print("Speler 1 is X, speler 2 is O")
    
    tos = randint(0, 1)
    if tos == 0:
        print("Speler 1 is Mens")
        player1 = HumanPlayer.HumanPlayer("X")
        player2 = RandomPlayer.RandomPlayer("O")
    else:
        print("Speler 1 is Computer")
        player1 = RandomPlayer.RandomPlayer("X")
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
    
    size_game = randint(3, 6)
    boaerd = [[" " for _ in range(size_game)] for _ in range(size_game)]

    if (nog_een_keer == "j"):
        board = create_new_board(size_game)
    else:
        break
    
