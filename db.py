
import sys

def read_money():
    try:
        with open("money.txt", "r") as f:
            player_money = float(f.readline())
    except FileNotFoundError:
            print("The file is not found.  Ending game")
            sys.exit(1)
    return player_money

def write_money(player_money):
    try:
        with open('money.txt', 'w') as f:
            f.write(str(player_money))
    except FileNotFoundError:
            print("The file is not found.  Ending game")
            sys.exit(1)

