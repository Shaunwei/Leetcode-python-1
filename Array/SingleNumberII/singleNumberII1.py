#!/usr/bin/python

"""
Single Number II 

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumberII(self, A):
        ones = twos = threes = 0
        for i in xrange(len(A)):
            twos |= ones & A[i]
            ones ^= A[i]   
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones

if __name__=="__main__":
    A = [1,2,1,3,1,2,2]
    print Solution().singleNumberII(A)

"""
Bit operation.
No extra memory used.
'ones' stands for bitmask only appears once in i-th position.
'twos' stands for bitmask only appears twice in i-th position.
'threes' stands for bitmask only appears three times in i-th position.
When the bitmask in i-th position appears three times, set 'ones' and 'twos' to zero.
And the final answer is the 'ones'.
"""

