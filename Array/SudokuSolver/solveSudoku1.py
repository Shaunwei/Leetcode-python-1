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
        self.solveSudokuRec(board,0,0)
    
    def solveSudokuRec(self, board,row,col):
        nextRow, nextCol = row, col+1
        if row == 9: return True
        if col == 8: nextRow, nextCol = row+1, 0
        if board[row][col]!='.':
            return self.solveSudokuRec(board,nextRow,nextCol)
        for c in xrange(1,10):
            if self.validate(board,str(c),row,col):
                board[row][col] = str(c)
                if self.solveSudokuRec(board,nextRow,nextCol):
                    return True
                board[row][col] = '.'
        return False
    
    def validate(self, board, char, row, col):
        for i in xrange(9):
            if board[row][i] == char: return False
            if board[i][col] == char: return False
        rowGroup, colGroup = (row/3)*3, (col/3)*3 
        for i in xrange(rowGroup, rowGroup+3):
            for j in xrange(colGroup, colGroup+3):
                if board[i][j] == char: return False
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
    Solution().solveSudoku(board)
    for i in board: print i

"""
Using DFS. 
As the Sudoku has fixed size of board (9x9), the check procedure 
can be solved using just "for loop".
1. Check the rows and columns respectively, a mark array is used 
   to check the numbers.
2. Check the 3x3 blocks, also using a mark array.
"""

