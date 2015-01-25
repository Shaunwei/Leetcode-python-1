#!/usr/bin/python

"""
Jump Game II 

Given an array of non-negative integers, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        lenA, maxi, jumpNum = len(A), 0, 0
        if lenA == 1: return 0
        while True:
            jumpNum += 1
            for i in xrange(maxi + 1):
                maxi = max(maxi, i + A[i]); print jumpNum, maxi
                if maxi >= lenA - 1: return jumpNum

if __name__=="__main__":
    A = [2,3,1,1,4]
    print Solution().jump(A)

"""
Similar as Jump Game.  Store first step can reach maximum index 
and count the jump number, then go to the index and do the same 
till the last index.
"""
