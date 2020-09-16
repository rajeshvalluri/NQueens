# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:54:40 2020

@author: TT-PC
"""
class draw_board():

    def draw_board(board):
        maxboardsize = min(board.master.winfo_width(), board.master.winfo_height() - 70)
        cellsize = maxboardsize // board.size
        board.board_canvas.config(height=board.size*cellsize, width=board.size*cellsize)
        board.board_canvas.delete('all')
        #print("drawing now",board.queens,maxboardsize,board.master.winfo_width(),board.master.winfo_height() - 70)

        # color in black board cells
        for i in range(board.size):
            for j in range(board.size):
                if (i+j+board.size) % 2: # black cell
                    board.board_canvas.create_rectangle(i*cellsize, j*cellsize,
                                                       i*cellsize+cellsize, j*cellsize+cellsize,
                                                       fill='black')
            #print("Testing the i and j value,",i,j)    
            # draw a queen
            board.board_canvas.create_text(i*cellsize+cellsize//2, board.queens[i]*cellsize+cellsize//2,
                                           text=u'\u265B', font=('Arial', cellsize//2), fill='orange')
