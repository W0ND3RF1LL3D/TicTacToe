Welcome to my first project in Python!

Follow along with me as I teach myself how to create a Tic Tac Toe game.

5/27/2024 - After watching several hour long videos, I have the basic concepts of Python. Combining it with my prior knowledge in Java, 
I've come up with the idea that I need to create a class that will keep track of the board and the moves that are acted upon the board.
It will be easier when I create an array, so that the moves can be tracked. For now, this is only the rough draft.

Next implementations:
    play() function - allows the player to choose where they would like to play
    has_winner() function - checks if there has been a winner

5/28/2024 - Created a board class and added the play() function. I also implemented a display_board() function and create_new_board() 
functions that directly change the board.  I'll be marking up the code with comments to help readability probably tomorrow.

Next implementations:
    Something to help see if the move requested is already on the board. Most likely a function that returns a boolean. (on_board:boolean)
    I also need to figure out how to add in multiple constructors (default, 1 arg, and 2 arg)
    
5/30/2024 - Marked up the code with comments. As well as fixed the problem of Player 1 moves not showing on the board, but Computer moves were.
I just needed to change the input from a str to an int.

Next implementations:
    Getting the has_winner() function to work.
    Getting the on_board() function to work.
