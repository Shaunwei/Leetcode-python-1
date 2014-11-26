#!/usr/bin/python

"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from 
top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        # initial
        dp = [[0 for i in xrange(cols)] for j in xrange(rows)]
        dp[0][0] = grid[0][0]
        for i in xrange(1,cols): dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in xrange(1,rows): dp[i][0]=dp[i-1][0]+grid[i][0]
        # dp process
        for i in xrange(1,rows):
            for j in xrange(1,cols):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[rows-1][cols-1]

if __name__=="__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]] 
    print Solution().minPathSum(grid)

"""
Using DP. For example:
[]    []       []      []
[]    []       [i-1,j] []
[]    [i,j-1]  [i,j]   [] 
[]    []       []      []
Formula:
Init: A[0][i] = A[0][i-1]+grid[0][i]
      A[i][0] = A[i-1][0]+grid[i][0]
State Change func:
      A[i][j] = min(A[i-1][j],A[i][j-1])+grid[i][j])
"""


