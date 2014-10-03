#!/usr/bin/python

"""
Sqrt(x) 

Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left, right = 0, 46340 # sqrt(MAX_INT) is 46340
        while left <= right:
            mid = (left+right) / 2
            if mid*mid <= x < (mid+1)*(mid+1): return mid
            elif mid*mid > x: right = mid - 1
            else:  left = mid + 1

if __name__=="__main__":
    x = 9
    print Solution().sqrt(x)

"""
Using binary search.
"""
