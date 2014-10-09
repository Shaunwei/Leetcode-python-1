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
        for layer in xrange(n/2):
            first = layer
            last  = n-1-layer 
            for i in xrange(first,last):
                offset = i - first
                top = matrix[first][i]
                # left to top            
                matrix[first][i] = matrix[last-offset][first]
                # bottom to top
                matrix[last-offset][first] = matrix[last][last-offset]
                # right to bottom
                matrix[last][last-offset] = matrix[i][last]
                # top to right
                matrix[i][last] = top
        return matrix

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]] 
    Solution().rotate(matrix)
    print matrix

"""
The idea is to rotate the matrix according to layers. 
For the nth layer(the out layer), rotate 90 degree is 
to move all the elements n times in a circle. In each layer, 
the rotation can be performed by first swap 4 corners, 
then swap 4 elements next to corner until the end of each line.
"""