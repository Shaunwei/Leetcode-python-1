#!/usr/bin/python

"""
Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = bin(int(a,2)+int(b,2))
        return c[2:]

if __name__=="__main__":
    a = "11"
    b = "1"
    print Solution().addBinary(a,b)

