#!/usr/bin/python

"""
Jump Game

Given an array of non-negative integers, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxj = 0
        for i in xrange(len(A)):
            if i <= maxj:
                maxj = max(maxj, A[i]+i)
                if maxj >= len(A)-1:
                    return True
    	return False

if __name__=="__main__":
    A = [3,2,1,0,4] # [2,3,1,1,4] # 
    print Solution().canJump(A)

"""
Note that the A[i] means the maximum jump length. In other words, 
it is possible that we move j steps (<A[i]) when we at A[i], 
e.g. if A[i]=2, we can move either 1 or 2 steps.
"""
