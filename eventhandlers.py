# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:25:28 2020

@author: TT-PC
"""
from solutions import *
from solutions_rec import *
from draw_board import draw_board
from time import time
from tkinter import *
from tkinter import ttk, messagebox
class eventhandlers ():
    def solution_callback(board,N):
        positions = board.solutions
        if (positions == []):
            size = 0
        else:
            size = len(positions[0])
        try:
            input_val = int(N)
        except:
            messagebox.showerror(title='Invalid Input',
                                 message='Must enter a number for N.')
            return
    
        # check if N has changed or if this is first run
        if size != input_val or positions == []:
            if 4 > input_val:
                messagebox.showerror(title='Invalid Value for N',
                                     message='N must be greater than 4.')
            else:
                start_time = time()
                positions = solutions_rec.check_combinations(input_val)
                #positions = solutions.check_combinations(input_val)

                board.index = 0
                board.solutions = positions
                # calculate new list of solutions
    
                elapsed_time = time() - start_time
                board.time_var.set('{0:.3f}s'.format(elapsed_time))
        else:
            board.index += 1
        #print("before",board.index, len(positions))
        board.queens = board.solutions[board.index % len(positions)]
        board.size = len(board.queens)
        board.solution_var.set('{0}/{1}'.format(board.index % len(positions) + 1, len(positions)))
        draw_board.draw_board(board)
        return