#!/usr/bin/python

"""
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        rowSize, colSize = len(matrix), len(matrix[0])
        leftI = leftJ = 0
        rightI, rightJ = rowSize-1, colSize-1
        while leftI*colSize+leftJ <= rightI*colSize+rightJ:
            mid = (leftI*colSize+leftJ + rightI*colSize+rightJ) / 2
            midI = mid / colSize
            midJ = mid % colSize
            if matrix[midI][midJ] == target: return True
            elif matrix[midI][midJ] < target:
                leftI = (mid+1) / colSize
                leftJ = (mid+1) % colSize
            else:
                rightI = (mid-1) / colSize
                rightJ = (mid-1) % colSize
        return False
    
if __name__=="__main__":
    A = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 11
    print Solution().searchMatrix(A,target)

"""
Binary search, just convert 2D coordinate to linear coordinate.
"""

