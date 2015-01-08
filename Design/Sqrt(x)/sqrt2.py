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
        i, j = 0, x/2+1
        while i <= j:
            mid = (i + j) / 2
            if mid * mid == x: return mid
            if mid * mid < x: i = mid + 1
            else: j = mid - 1
        return int(j)

if __name__=="__main__":
    x = 9
    print Solution().sqrt(x)

"""
Using Newton's method: a = (a + x / a) / 2
"""
