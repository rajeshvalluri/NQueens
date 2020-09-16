# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:57:48 2020

@author: RValluri1
"""
from draw_board import draw_board
from tkinter import ttk, messagebox
# Generalised N-Queens problem
from solutions import solutions
from solutions import *
from eventhandlers import *
class board():
    def __init__(self,master):
        self.index = 0 #the nth of the possibile arrangement of queens
        self.solutions = [] # initializing the solutions array
        self.size = 0  #the size of the chess board, as in 4X4, or 6X6 etc. just one number.
        self.queens = [] #The current state of the chessboards with queens on them. an array of position values
        # build gui
        self.master = master
        self.master.title('NQueens')
        self.master.configure(background='#e1d8b9')
        self.master.minsize(400, 470)
        self.master.resizable(True, True)
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9')
                    
        self.board_canvas = Canvas(self.master)
        self.board_canvas.pack()
    
        self.controls_frame = ttk.Frame(self.master)
        self.controls_frame.pack(side=TOP, pady=10)
    
        ttk.Label(self.controls_frame, text='Number of Queens:',
                  font='Verdana 10 bold').grid(row=0, column=0)
        self.n_var = StringVar()
        self.n_var.set(self.size)
        Spinbox(self.controls_frame, from_=4, to=99, width=2,
                font='Verdana 10 bold', textvariable=self.n_var).grid(row=0, column=1)
        #dummy call was necessary because we can't send arguments to functions from buttonclicks directly
        ttk.Button(self.controls_frame, text = 'Next Solution',command=self._dummy_call).grid(row=1, column=0, columnspan=2)
        ttk.Label(self.controls_frame).grid(row=0, column=2, padx=10) # spacer
    
        self.solution_var = StringVar()
        self.time_var = StringVar()
        self.solution_var.set('--')
        self.time_var.set('--')
        self.n_var.set(4)
        ttk.Label(self.controls_frame, text='Solution:',
                  font='Verdana 10 bold').grid(row=0, column=3, sticky=(E))
        ttk.Label(self.controls_frame, textvariable=self.solution_var,
                  font='Verdana 10').grid(row=0, column=4, sticky=(W))
        ttk.Label(self.controls_frame, text='Elapsed Time:',
                  font='Verdana 10 bold').grid(row=1, column=3, sticky=(E))
        ttk.Label(self.controls_frame, textvariable = self.time_var,
                  font='Verdana 10').grid(row=1, column=4, sticky=(W))
        self.master.update() #This line is necessary to get the widget to update its width and legth
        self._dummy_call() #initial layout of the board
    
    def _dummy_call(self):
        #print(int(self.n_var.get()))
        eventhandlers.solution_callback(self,int(self.n_var.get()))
        
