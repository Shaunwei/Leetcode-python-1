#!/usr/bin/python

"""
N-Queens 

The n-queens puzzle is the problem of placing n queens on an nXn chessboard such 
that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res
     
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [ ['.' for j in xrange(n)] for i in xrange(n) ]
            for i in xrange(n): 
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        # try to put a Queen in (currQueenNum, 0), (currQueenNum, 1), ..., (currQueenNum, n-1)
        for i in xrange(n):
            valid = True  # test whether board[currQueenNum] can be i or not
            for k in xrange(currQueenNum):
                # check column
                if board[k] == i: valid = False; break
                # check dianogal
                if abs(board[k] - i) == currQueenNum - k: valid = False; break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)
    	

if __name__=="__main__":
    n = 2 # 4
    print Solution().solveNQueens(n)

"""
The classic recursive problem.
1. Use a int vector to store the current state,  A[i]=j refers that 
the ith row and jth column is placed a queen.
2. Valid state:  not in the same column, which is A[i]!=A[current], 
not in the same diagonal direction: abs(A[i]-A[current]) != r-i

3. Recursion: 
       Start: placeQueen(0,n)
        if current ==n then print result
        else
            for each place less than n,
                place queen
                if current state is valid, then place next queen place Queen(cur+1,n)
           end for
        end if
"""