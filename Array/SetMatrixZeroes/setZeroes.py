#!/usr/bin/python

"""
Set Matrix Zeroes  

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rownum, colnum = len(matrix), len(matrix[0])
        rowZeros = set()
        colZeros = set()
        for i in xrange(rownum):
            for j in xrange(colnum):
                if matrix[i][j] == 0:
                    rowZeros.add(i); colZeros.add(j)
        for i in rowZeros:
            for j in xrange(colnum):
                matrix[i][j] = 0
        for j in colZeros:
            for i in xrange(rownum):
                matrix[i][j] = 0

if __name__=="__main__":
    s = [[1,2,0,3],[1,3,4,5],[2,3,6,7],[1,3,4,5]] 
    Solution().setZeroes(s)
    print s
