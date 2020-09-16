# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:00:54 2020

@author: RValluri1
"""
from itertools import permutations, combinations
class solutions_rec():
        def check_combinations_int(totalSolutions,sln,CurrColumn,N):
        #NXN board, starting with index 0 for first column.
            lclSolution = sln.copy() # assign the semi filled solution to a local solution
            if (CurrColumn == N):
        #        print ("Reached the last level")
        #        print(lclSolution)
                totalSolutions.append(lclSolution)
            else:
                for rows in range(N):
                    #lclSolution = sln.copy()
                    #Check if the row has already been used to place a queen
                    if (rows not in sln):
                        lclSolution = sln.copy()
                        lclSolution.append(rows)
                        flag = solutions_rec.check_solution(lclSolution)
                        if (flag == True):
                            solutions_rec.check_combinations_int(totalSolutions,lclSolution,CurrColumn+1,N)
                        else:
                            #print("Moving On")
                            pass
                           
        def check_solution(sln):
            #print("the set now is",sln)
            for row1, row2 in combinations(range(len(sln)),2):
                #print(row1,row2,sln[row1],sln[row2])
#                input("Press Enter to continue...")
                #Checking for the diagonal
                flag =  (abs(row1 - row2) - abs(sln[row1] - sln[row2]))
#                flag1 = abs(row1 - row2)
#                flag2 = abs(sln[row1] - sln[row2])
                if ( flag == 0):
                    return False
            return True
        def check_combinations(input_val):
            sln = []
            totalSolutions = []
            solutions_rec.check_combinations_int(totalSolutions,sln,0,input_val)
            return(totalSolutions)
    
#def main():
#    N = 10
#    sln = []
#    totalSolutions = []
#    checkSolutions(totalSolutions,sln,0,N)
#    print (totalSolutions)
#if __name__ == "__main__":
#    main()