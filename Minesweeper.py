from ctypes import sizeof
import tkinter as tk
import random

def setGame(difficulty):
    x = 0
    y = 0
    mines=0
    # Easy
    if difficulty == 0:
        # dimensions
        x = 10
        y = 8
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 10

    # Medium
    elif difficulty == 1:
        # dimensions
        x = 12
        y = 20
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 40

    #Hard
    else:
        # dimensions
        x = 20
        y = 24
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 99

    # Places locations for mines
    board = setMines(board, x, y, mines)

    # Test print
    for x in board:
        print(x)
    


def setMines(board, x, y, mines):
    for i in range(mines):
        pos = random.randrange(0,x*y-1)
        posx = int(pos / x)  
        posy = pos % x
        while (board[posx][posy] == "*"):
            pos = random.randrange(0,x*y-1)
            posx = int(pos / x)  
            posy = pos % x
        (board[posx][(posy)]) = "*"
        
    return board


setGame(2)

window = tk.Tk()

window.mainloop()