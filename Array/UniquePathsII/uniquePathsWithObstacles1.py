#!/usr/bin/python

"""
Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
    	if obstacleGrid[0][0] == 1: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        board = [[0 for i in xrange(n)] for j in xrange(m)]
        board[0][0] = 1
        for i in xrange(1,m): 
        	if obstacleGrid[i][0] != 1:
        		board[i][0] = board[i-1][0] 
        for j in xrange(1,n): 
        	if obstacleGrid[0][j] != 1:
        		board[0][j] = board[0][j-1]
        for i in xrange(1,m):
            for j in xrange(1,n):
            	if obstacleGrid[i][j] != 1:
                	board[i][j] = board[i-1][j] + board[i][j-1]
                else: 
                	board[i][j] = 0
        return board[m-1][n-1] 

if __name__=="__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print Solution().uniquePathsWithObstacles(obstacleGrid)

"""
Using DP, initiialize first row or first column when meet an obstacle, then stop 
process since the path is block.  Same idea for the grid[i][j], if no obstacle then
grid[i][j] = grid[i-1][j]+grid[i][j-1], and if meet obstacle then grid[i][j] = 0.
"""

