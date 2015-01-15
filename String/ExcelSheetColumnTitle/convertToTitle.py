#!/usr/bin/python

"""
Excel Sheet Column Title 

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""

class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ''
        while num > 0:
            rem, num = num%26, num/26
            if rem == 0: res += 'Z'; num -= 1
            else:  res += chr(rem+ord('A')-1)
        return res[::-1]

if __name__=="__main__":
    a = 52
    print Solution().convertToTitle(a)

"""
In Excel, the range is A~Z, AA~ZZ, AAA~ZZZ. So the problem will be 26-base convert
problem, mod 26 every time, and if remainder is zero, needs to num - 1.
"""