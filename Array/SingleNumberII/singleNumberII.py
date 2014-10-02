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
        bit = [0 for i in xrange(32)]
        for x in A:
            for i in xrange(32):
                if x & (1 << i) == 1 << i: bit[i] += 1
        res = 0
        if bit[31] % 3 == 0: # posivie
            for i in xrange(31): 
                if bit[i] % 3 == 1: res += 1 << i    
        else: # negative
            for i in xrange(31): 
                if bit[i] % 3 == 0: res += 1 << i
            res = -(res + 1)
        return res
if __name__=="__main__":
    A = [1,2,1,3,1,2,2]
    print Solution().singleNumberII(A)

"""
Need to consider these cases:
1. irregular input but valid, such as "-3924x8fc","  +  413";
2. invalid format: such as " ++c", " ++1"
3. overflow integer range: "2147483648".
"""

