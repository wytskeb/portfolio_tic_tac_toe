from random import randint
n = randint(3, 6)

aantal_x = 0
aantal_o = 0

board = [[" " for _ in range(n)] for _ in range(n)]

def print_board(board):
    print("X  -", end="")
    print("-" * 2 * n)
    for row in board:
        print("|  |", end="")
        print("|".join(row) + "|")
        print("|  -", end="")
        print("-" * 2 * n)
    print ("v/Y--------->")

def create_new_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


def check_winner(board):
    for i in range(n):
        if board[i][0] != " " and all(board[i][j] == board[i][0] for j in range(n)):
            return board[i][0]
        if board[0][i] != " " and all(board[j][i] == board[0][i] for j in range(n)):
            return board[0][i]
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(n)):
        return board[0][0]
    if board[0][n-1] != " " and all(board[i][n-1-i] == board[0][n-1] for i in range(n)):
        return board[0][n-1]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    move = 0
    while True:
        player_move = input(f"Speler {move+1}, geef je X positie: ")
        x = player_move
        player_move = input(f"Speler {move+1}, Geef je Y positie: ")
        y = player_move
        try :
            x = int(x)
            y = int(y)
        except ValueError:
            print("Ongeldige positie")
            continue
        if (x < 1 or x > n) or (y < 1 or y > n):
            print("Ongeldige positie")
            continue
        if board[x-1][y-1] != " ":
            print("Positie is al bezet")
            continue
        print(move)
        if move == 0:
            sine = "X"
        else:
            sine = "O"
        board[x-1][y-1] = sine
        print_board(board)
        move += 1
        move = move % 2
        if check_winner(board) == sine:
            print(f"{sine} heeft gewonnen!")
            return sine
        if check_draw(board):
            print("Gelijkspel!")
            return None

while True:
    print(f"Het spel begint! We spelen op een {n} X {n} bord. Wie het eerst {n} op rij heeft!")
    print_board(board)

    gewonnen = play_game()
    if (gewonnen == "X"):
        print("Speler 1 heeft gewonnen!")
        aantal_x += 1
    elif (gewonnen == "O"):
        print("Speler 2 heeft gewonnen!")
        aantal_o += 1

    nog_een_keer = input (f"Het staat {aantal_x} / {aantal_o}. Nog een keer? (j/n) ")
    n = randint(3, 6)
    boaerd = [[" " for _ in range(n)] for _ in range(n)]

    if (nog_een_keer == "j"):
        board = create_new_board(n)
    else:
        break
    
