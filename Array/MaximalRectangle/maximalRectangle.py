#!/usr/bin/python

"""
Maximal Rectangle 

Given a 2D binary matrix filled with 0's and 1's, find the largest 
rectangle containing all ones and return its area.
"""

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0: return 0
        maxarea, rlen, clen = 0, len(matrix), len(matrix[0])
        m = [[0 for i in xrange(clen+1)]for i in xrange(rlen+1)]
        for i in xrange(rlen):
            for j in xrange(clen-1,-1,-1):
                m[i][j] = 1+m[i][j+1] if matrix[i][j]=='1' else 0
               
        for i in xrange(clen):
            p, s = 0, []  
            while p != len(m):
                if not s or m[p][i] >= m[s[-1]][i]: 
                    s.append(p); p += 1
                else: 
                    t = s.pop() 
                    maxarea = max(maxarea,m[t][i]*(p if not s else p-s[-1]-1))
        return maxarea

if __name__=="__main__":
    matrix = [['0','1','1','1','0','0','0','0'],
              ['1','1','1','1','0','0','0','0'],
              ['1','1','1','1','1','1','1','0'],
              ['1','0','0','0','0','1','1','0']]
    print Solution().maximalRectangle(matrix)

"""
An O(mn) solution idea:
Transform this problem to the 1-dimensional one, and then 
use O(n) algorithm to solve it by each column (total m). 
("Largest Rectangle in Histogram" problem)

Problem solving:
Suppose the matrix has m rows and n columns. The following will discuss an 
efficient algorithm which has time complexity O(mn). To begin with, 
we show some properties of all 1's largest rectangle.

Definition:
1. Bar: A bar is a line of matrix elements being all 1's. 
Bar could be horizontal or vertical according to its orientation.
2. Histogram: A histogram is one horizontal bar being the base concatenating with 
a number of vertical bars ('base' means that the bottoms of vertical bars are located 
on the horizontal bar). We call a histogram base-k histogram if its base horizontal 
bar is at k-th row. Moreover, if a histogram cannot be contained within any other 
histogram except itself, it is a "maximal histogram".
i.e.  maximal histograms in a matrix:
    _________ 
 0 | 1  1  1 | 0  0  0  0
 __|         |
|1 | 1  1  1 | 0  0  0  0
|  |         |________
|1 | 1  1  1   1 |1  1| 0
|__|_____________|____|
|1 | 0  0  0   0 |1  1| 0
|__|_____________|____|

Theorem 1: The largest rectangle is contained within a maximal histogram.

Theorem 2: For each k, any two base-k maximal histograms do not intersect.
"""