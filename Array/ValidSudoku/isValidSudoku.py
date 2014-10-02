#!/usr/bin/python

"""
Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled 
with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. 
Only the filled cells need to be validated.
"""

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row
        for row in board:
            dup = []
            for i in row:
                if i != '.':
                    if i not in dup: dup.append(i)
                    else: return False
        # check column
        for i in xrange(9):
            dup = []
            for j in xrange(9):
                k = board[j][i]
                if k != '.':
                    if k not in dup: dup.append(k)
                    else: return False
        # check 3x3 subboard
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                dup = []
                for m in [0, 1, 2]:
                    for n in [0, 1, 2]:
                        k = board[i+m][j+n]
                        if k != '.':
                            if k not in dup: dup.append(k)
                            else: return False
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
    for i in board: print i
    print Solution().isValidSudoku(board)

"""
As the Sudoku has fixed size of board (9x9), the check procedure 
can be solved using just "for loop"
1. Check the rows and columns respectively, a mark array is used 
to check the numbers.
2. Check the 3x3 blocks, also using a mark array.
"""

