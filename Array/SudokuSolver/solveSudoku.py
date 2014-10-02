#!/usr/bin/python

"""
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # appearance of 1-9 in row 1-9
        r = [[False for i in xrange(9)] for j in xrange(9)] 
        # appearance of 1-9 in col 1-9
        c = [[False for i in xrange(9)] for j in xrange(9)] 
        # appearance of 1-9 in grid 1-9
        g = [[[False for i in xrange(9)] for j in xrange(3)] for k in xrange(3)]
        # init r, c, g
        for i in xrange(9):
          for j in xrange(9):
            if board[i][j] != '.':
              r[i][int(board[i][j])-int('1')] = True
              c[j][int(board[i][j])-int('1')] = True
              g[i/3][j/3][int(board[i][j])-int('1')] = True
        self.sudokuDFS(board,0,0,r,c,g)
    
    def sudokuDFS(self, board, i, j, r, c, g):
        k = 0
        for m in xrange(i,9):
          n = j if m==i else 0
          while n < 9:
            if board[m][n] == '.':
                while k < 9:
                    if not r[m][k] and not c[n][k] and not g[m/3][n/3][k]:
                      r[m][k] = c[n][k] = g[m/3][n/3][k] = True
                      board[m][n] = str(k+1)
                      if self.sudokuDFS(board, m, n, r, c, g):
                        return True
                      board[m][n] = '.'
                      r[m][k] = c[n][k] = g[m/3][n/3][k] = False
                    k += 1
                if k == 9:  # no such number possible, dead
                    return False
            n += 1
        return True
        
if __name__=="__main__":
    board = [['5','3','.','.','7','.','.','.','.'],\
             ['6','.','.','1','9','5','.','.','.'],\
             ['.','9','8','.','.','.','.','6','.'],\
             ['8','.','.','.','6','.','.','.','3'],\
             ['4','.','.','8','.','3','.','.','1'],\
             ['7','.','.','.','2','.','.','.','6'],\
             ['.','6','.','.','.','.','2','8','.'],\
             ['.','.','.','4','1','9','.','.','5'],\
             ['.','.','.','.','8','.','.','7','9']]
    #for i in board: print i
    Solution().solveSudoku(board)
    for i in board: print i

"""
As the Sudoku has fixed size of board (9x9), the check procedure 
can be solved using just "for loop"
1. Check the rows and columns respectively, a mark array is used 
to check the numbers.
2. Check the 3x3 blocks, also using a mark array.
"""

