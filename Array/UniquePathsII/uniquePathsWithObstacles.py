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
    	# base case
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        board = [[0 for i in xrange(col)] for j in xrange(row)]
        for i in xrange(row): 
        	if obstacleGrid[i][0] == 0: board[i][0] = 1
        	else: break
        for j in xrange(col): 
        	if obstacleGrid[0][j] == 0: board[0][j] = 1
        	else: break
        # dp process
        for i in xrange(1,row):
            for j in xrange(1,col):
            	board[i][j] = 0 if obstacleGrid[i][j]==1 else board[i-1][j]+board[i][j-1]
        return board[row-1][col-1] 

if __name__=="__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print Solution().uniquePathsWithObstacles(obstacleGrid)

"""
Using DP, initiialize first row or first column when meet an obstacle, then stop 
process since the path is block.  Same idea for the grid[i][j], if no obstacle then
grid[i][j] = grid[i-1][j]+grid[i][j-1], and if meet obstacle then grid[i][j] = 0.
"""

