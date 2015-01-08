#!/usr/bin/python

"""
Rotate Image 

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in xrange(n/2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        return matrix

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]] 
    Solution().rotate(matrix)
    print matrix

"""
In-place way is:
Swap elements by diagonal line(matrix[0][n-1] to matrix[n-1][0]),
then swap elements again by horizontal middile line (n+1)/2.
"""