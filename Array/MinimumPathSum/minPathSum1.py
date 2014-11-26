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
        rows, cols, maxint = len(grid), len(grid[0]), 10**10
        if rows==0 or cols==0: return 0
        step = [maxint for i in xrange(cols)]; step[0]=0
        for i in xrange(rows):
            step[0] = step[0]+grid[i][0]
            for j in xrange(1,cols):
                step[j] = min(step[j],step[j-1])+grid[i][j]
        return step[cols-1]

if __name__=="__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]] 
    print Solution().minPathSum(grid)

"""
This version is no need extra two-d array.
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


