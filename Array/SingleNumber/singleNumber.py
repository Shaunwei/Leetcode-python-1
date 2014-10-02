#!/usr/bin/python

"""
Single Number 

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A: res ^= i
        return res

if __name__=="__main__":
    A = [1,2,1,3,4,2,3,4,5]
    print Solution().singleNumber(A)

"""
The requirement is O(n) time and O(1) space.
Thus, the  "first sort and then find " way is not working.
Also the "hash map" way is not working.

Since we can not sort the array, we shall find a cumulative way, which is not about the ordering.

XOR is a good way, we can use the property that A XOR A = 0, and A XOR B XOR A = B.

So, the code becomes extremely easy.
"""

