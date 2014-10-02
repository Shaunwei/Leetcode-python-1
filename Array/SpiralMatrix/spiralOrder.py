#!/usr/bin/python

"""
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
      if len(matrix) == 0: return []
      maxUp, maxLeft, result = 0, 0, []
      maxDown, maxRight = len(matrix)-1, len(matrix[0])-1
      # 0 go right, 1 go down, 2 go left, 3 go up
      direct = 0 
      while True:
        if direct == 0: # go right
          for i in xrange(maxLeft, maxRight + 1): 
            result.append(matrix[maxUp][i])
          maxUp += 1
        elif direct == 1: # go down
          for i in xrange(maxUp, maxDown + 1): 
            result.append(matrix[i][maxRight])
          maxRight -= 1
        elif direct == 2: # go left
          for i in reversed(xrange(maxLeft, maxRight + 1)): 
            result.append(matrix[maxDown][i])
          maxDown -= 1
        else: # go up
          for i in reversed(xrange(maxUp, maxDown + 1)): 
            result.append(matrix[i][maxLeft])
          maxLeft += 1
        if maxUp > maxDown or maxLeft > maxRight: 
          return result
        direct = (direct + 1) % 4
      return result

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print Solution().spiralOrder(matrix)


"""
0,1,2,3 four values are used to indicates direction: 
maxUp, maxDown, maxLeft, maxRight four variables are 
used to record four boundaries. When maxUp > maxDown or 
maxLeft > maxRight program can return.
"""

