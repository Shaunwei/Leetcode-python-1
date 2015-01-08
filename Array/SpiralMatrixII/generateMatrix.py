#!/usr/bin/python

"""
Spiral Matrix II 

Given an integer n, generate a square matrix filled with elements from 
1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        direct = 0 # 0 go right, 1 go down, 2 go left, 3 go up
        maxUp = maxLeft = 0
        maxDown = maxRight = n - 1
        matrix = [[0 for j in xrange(n)]for i in xrange(n)]
        curr = 0
        while True:
            if direct == 0: # go right
                for i in xrange(maxLeft, maxRight + 1): 
                    curr += 1; matrix[maxUp][i] = curr
                maxUp += 1
            elif direct == 1: # go down
                for i in xrange(maxUp, maxDown + 1): 
                    curr += 1; matrix[i][maxRight] = curr
                maxRight -= 1
            elif direct == 2: # go left
                for i in reversed(xrange(maxLeft, maxRight + 1)): 
                    curr += 1; matrix[maxDown][i] = curr
                maxDown -= 1
            else: # go up
                for i in reversed(xrange(maxUp, maxDown + 1)): 
                    curr += 1; matrix[i][maxLeft] = curr
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight: 
                return matrix
            direct = (direct + 1) % 4
        return matrix

if __name__=="__main__":
    n = 3
    print Solution().generateMatrix(n)


"""
Same idea as Spiral Matrix.
"""

