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
        carry, result = 0, ''
        i, j = len(a)-1, len(b)-1
        while i>=0 or j>=0:
            ai = int(a[i]) if i>=0 else 0
            bi = int(b[j]) if j>=0 else 0
            val = (ai+bi+carry) % 2
            carry = (ai+bi+carry) / 2
            result = str(val) + result
            i, j = i-1, j-1
        if carry == 1:
            result = '1' + result
        return result

if __name__=="__main__":
    a, b = '11', '1'
    print Solution().addBinary(a,b)

