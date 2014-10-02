#!/usr/bin/python

"""
Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        numstr = str(x)
        if x >= 0: return int(numstr[::-1])
        else: return int(numstr[0]+numstr[1:][::-1])

if __name__=="__main__":
    x1 = 123
    x2 = -123
    print Solution().reverse(x1)
    print Solution().reverse(x2)