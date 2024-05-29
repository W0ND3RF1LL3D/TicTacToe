import random


class Board:
    def __int__(self):
        self.player = ""
        self.opponent = ""
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def __init__(self, player, vs_player):
        self.player = player
        self.opponent = vs_player
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def create_new_board(self):
        new_board = f"""
      {self.board[0][0]}  | {self.board[0][1]}   | {self.board[0][2]}
    ---------------
      {self.board[1][0]}  |  {self.board[1][1]}  | {self.board[1][2]}
    ---------------
      {self.board[2][0]}  | {self.board[2][1]}   | {self.board[2][2]}
"""
        return new_board

    def play(self, its_player1_turn, has_no_winner):
        if its_player1_turn and has_no_winner:
            turn = input("Where would you like to play? ")

            if turn == "help":
                self.display_help()
                turn = input("Where would you like to play? ")

            return f"{self.player} chose to go in spot {turn}"
        elif self.opponent != "Computer" and has_no_winner:
            turn = input("Where would you like to play?")

            if turn == "help":
                self.display_help()
                turn = input("Where would you like to play? ")

            return f"{self.opponent} chose to go in spot {turn}"
        elif self.opponent == "Computer" and has_no_winner:
            turn = random.randint(1, 9)
            return f"Computer chose to go in spot {turn}"
        else:
            print("")

    def display_board(self):
        print(f"""
      {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}
    ---------------
      {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}
    ---------------
      {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}
    """)

    def display_help(self):
        print(f"""
      1  |  2  |  3
    ----------------
      4  |  5  |  6
    ----------------
      7  |  8  |  9
        """)


def start_game():
    print("Welcome to the world of Tic Tac Toe!")
    answer = input("Would you like to start a new game (Yes/No)? ")

    if answer.lower() == "yes":
        player_1 = input("Great! Can we start with the name of player 1? ")

    answer = input("Will you be playing with another player (Yes/No)? ")

    if answer.lower() == "yes":
        opponent = input("What is the name of player 2? ")
    else:
        opponent = "Computer"

    return player_1

player1 = start_game()

new_game = Board(player1, "Computer")


print(new_game.create_new_board())

for number in range(0, 5):
    print(new_game.play(True, True))
    new_game.display_board()
    print(new_game.play(False, True))
    new_game.display_board()
