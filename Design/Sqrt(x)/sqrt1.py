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
        if x == 0: return 0
        last, res = 0.0, 1.0
        while last != res: last, res = res, (res+x/res)/2
        return int(res)

if __name__=="__main__":
    x = 9
    print Solution().sqrt(x)

"""
Using Newton's method: a = (a + x / a) / 2
"""
