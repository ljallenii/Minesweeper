import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

class Game(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        Frame.grid(self)
        ttk.Button(self, text="Easy", command=self.easyModeButton).grid(column=1, row=0)
        ttk.Button(self, text="Medium", command=self.medModeButton).grid(column=1, row=1)
        ttk.Button(self, text="Hard", command=self.hardModeButton).grid(column=1, row=2)

    def easyModeButton(self):
        self.master.geometry("400x400")

        x = 10
        y = 8
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 10

        board = self.setMines(board, x, y, mines)

        for i in board:
            print(i)


    def medModeButton(self):
        self.master.geometry("600x600")

         # dimensions
        x = 12
        y = 20
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 40

        board = self.setMines(board, x, y, mines)

        for i in board:
            print(i)

    def hardModeButton(self):
        self.master.geometry("800x800")

        # dimensions
        x = 20
        y = 24
        # Creates a board in terminal of location of bombs
        board = [[None for i in range(x)] for j in range(y)]
        mines = 99

        board = self.setMines(board, x, y, mines)

        for i in board:
            print(i)

    def setMines(self, board, x, y, mines):
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


window = Tk()
game = Game(window)

window.wm_title("Minesweeper")

#easyResize = window.geometry("400x400")
#medResize = window.geometry("600x600")


#ttk.Button(frm, text="Easy", command=easyResize).grid(column=1, row=0)
#ttk.Button(frm, text="Medium", command=medResize).grid(column=1, row=1)
#ttk.Button(frm, text="Hard").grid(column=1, row=2)

ttk.Button(game, text="Quit", command=window.destroy).grid(column=1, row=4)


window.mainloop()