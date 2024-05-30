import random


class Board:
    # A constructor for having the class ask for player and opponent info
    # Still in development
    def __int__(self):
        self.player = ""
        self.opponent = ""
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Current constructor in use
    # Previously asked for player and opponent info
    def __init__(self, player, vs_player):
        self.player = player
        self.opponent = vs_player
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Function for creating a new game
    # Will be used for restarting as well
    def create_new_board(self):
        new_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.board = new_board
        return self.board

    def has_winner(self):
        if self.board[0][0] != " ":
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                return False
            elif self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
                return False
            elif self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
                return False
        if self.board[1][1] != " ":
            if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
                return False
            elif self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
                return False
            elif self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
                return False
        if self.board[2][2] != " ":
            if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
                return False
            elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
                return False

    # Function to check if the current move is already on the board, returning boolean
    def on_board(self, move):
        if move == 1:
            if self.board[0][0] == " ":
                return False
        elif move == 2:
            if self.board[0][1] == " ":
                return False
        elif move == 3:
            if self.board[0][2] == " ":
                return False
        elif move == 4:
            if self.board[1][0] == " ":
                return False
        elif move == 5:
            if self.board[1][1] == " ":
                return False
        elif move == 6:
            if self.board[1][2] == " ":
                return False
        elif move == 7:
            if self.board[2][0] == " ":
                return False
        elif move == 8:
            if self.board[2][1] == " ":
                return False
        elif move == 9:
            if self.board[2][2] == " ":
                return False
        else:
            return True

    # Function to take info about the move being made, and alter the game board accordingly
    def play_on_board(self, move, player1_turn):
        move = (int(move))
        if player1_turn:
            if move == 1:
                self.board[0][0] = "X"
            elif move == 2:
                self.board[0][1] = "X"
            elif move == 3:
                self.board[0][2] = "X"
            elif move == 4:
                self.board[1][0] = "X"
            elif move == 5:
                self.board[1][1] = "X"
            elif move == 6:
                self.board[1][2] = "X"
            elif move == 7:
                self.board[2][0] = "X"
            elif move == 8:
                self.board[2][1] = "X"
            elif move == 9:
                self.board[2][2] = "X"
            else:
                print("Something else bad happened")
        elif not player1_turn:
            if move == 1:
                self.board[0][0] = "O"
            elif move == 2:
                self.board[0][1] = "O"
            elif move == 3:
                self.board[0][2] = "O"
            elif move == 4:
                self.board[1][0] = "O"
            elif move == 5:
                self.board[1][1] = "O"
            elif move == 6:
                self.board[1][2] = "O"
            elif move == 7:
                self.board[2][0] = "O"
            elif move == 8:
                self.board[2][1] = "O"
            elif move == 9:
                self.board[2][2] = "O"
        else:
            print("Nothing happened")

    # Function for asking player(s) for their next move
    # It also acts as the computer making their next move
    # Still need to implement checking if the move has already been made
    def play(self, its_player1_turn):
        if its_player1_turn:
            turn = input("Where would you like to play? ")
            if turn == "help":
                self.display_help()
                turn = input("Where would you like to play? ")
            # elif self.on_board(turn):
            # while self.on_board(turn):
            # turn = input("Where would you like to play? ")
            else:
                self.play_on_board(turn, True)
            return f"{self.player} chose to go in spot {turn}"
        elif self.opponent != "Computer":
            turn = input("Where would you like to play? ")
            while turn == "help":
                self.display_help()
                turn = input("Where would you like to play? ")
            # elif self.on_board(turn):
                # while self.on_board(turn):
                # turn = input("Where would you like to play? ")
            self.play_on_board(turn, False)
            return f"{self.opponent} chose to go in spot {turn}"
        elif self.opponent == "Computer":
            turn = random.randint(1, 9)
            while self.on_board(turn):
                turn = random.randint(1, 9)
            self.play_on_board(turn, False)
            return f"Computer chose to go in spot {turn}"
        else:
            print("Something bad happened")

    # Function for showing the current state of the board to the player
    # Used inbetween moves
    def display_board(self):
        print(f"""
      {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}
    ----------------
      {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}
    ----------------
      {self.board[2][0]}  |  {self.board[2][1]}  | {self.board[2][2]}
    """)

    # Function for aiding the player in making their next move
    def display_help(self):
        print(f"""
      1  |  2  |  3
    ----------------
      4  |  5  |  6
    ----------------
      7  |  8  |  9
        """)


# Function outside of Board class for asking for player/opponent info
# Still need to implement getting player 2 info
def start_game():
    print("Welcome to the world of Tic Tac Toe!")
    answer = input("Would you like to start a new game (Yes/No)? ")

    if answer.lower() == "yes":
        player_1 = input("Great! Can we start with the name of player 1? ")

        answer = input("Will you be playing with another player (Yes/No)? ")

        if answer.lower() == "yes":
            opponent = input("What is the name of player 2? ")
            new_game = Board(player_1, opponent)

            new_game.create_new_board()
            new_game.display_board()

            while not new_game.has_winner():
                print(new_game.play(True))
                new_game.display_board()
                print(new_game.play(False))
                new_game.display_board()
        else:
            opponent = "Computer"
            new_game = Board(player_1, opponent)

            new_game.create_new_board()
            new_game.display_board()

            while not new_game.has_winner():
                print(new_game.play(True))
                new_game.display_board()
                print(new_game.play(False))
                new_game.display_board()
    else:
        print("Okay! Maybe next time!")


# Testing code
start_game()
