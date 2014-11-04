#!/usr/bin/python

"""
N-Queens II 

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res
     
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n: self.res += 1; return
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
    n = 4 # 2
    print Solution().totalNQueens(n)

"""
This problem is the same idea as the N-Queens.
"""