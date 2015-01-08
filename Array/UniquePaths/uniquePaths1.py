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
        N = m - 1 + n - 1
        K = min(m, n) - 1
        result = 1 # calculate C(N, K)
        for i in xrange(K):
            result = result*(N-i)/(i+1)
        return result 

if __name__=="__main__":
    m, n = 7, 3 # 51, 9 # 
    print Solution().uniquePaths(m,n)

"""
m x n matrix to the end needs m-1 steps down and n-1 steps right,
so we need to calculate C(m-1+n-1,n-1) or C(m-1+n-1,m-1)
"""