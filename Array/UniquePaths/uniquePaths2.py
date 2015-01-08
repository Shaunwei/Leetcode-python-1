#!/usr/bin/python

"""
Unique Paths 

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        maxv = [0 for i in xrange(n)]
        maxv[0] = 1
        for i in xrange(m):
            for j in xrange(1,n):
                maxv[j] = maxv[j-1] + maxv[j]
        return maxv[n-1]
        

if __name__=="__main__":
    m, n = 7, 3 # 51, 9 # 
    print Solution().uniquePaths(m,n)

"""
One dimension DP: Step[i][j] = Step[i-1][j] + Step[i][j-1].
"""

