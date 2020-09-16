# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:55:06 2020

@author: RValluri1
"""
#from board import *
from itertools import permutations,combinations
class solutions():
    def check_combinations(size):
        combinations = permutations(range(size))
        valid_combinations = []
        for perms in combinations:
            #print(perms)
            if (solutions.is_valid_perm(perms)):
                valid_combinations.append(perms)
            #input("Press any key")
        return(valid_combinations)
    
    def is_valid_perm(perm):
        #print("the set now is",perm)
        for row1, row2 in combinations(range(len(perm)),2):
            #print(row1,row2,perm[row1],perm[row2])
            flag =  (abs(row1 - row2) - abs(perm[row1] - perm[row2]))
            if flag == 0:
                return False
        return True