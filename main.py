# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:38:03 2020

@author: RValluri1
"""
from board import *
from solutions import solutions
from tkinter import *
from tkinter import ttk, messagebox
from draw_board import draw_board
#from eventhandlers import *

def main():
    root = Tk()
    #Initialize a solution of required size
    #sols = solutions.check_combinations(8)
    #initialize a boarad, with "solutions" as arguments
    brd = board(root)
    root.mainloop()
if __name__ == "__main__":
    main()
