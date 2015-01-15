#!/usr/bin/python

"""
Excel Sheet Column Number 

Related to question 'Excel Sheet Column Title'

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        for i in xrange(len(s)):
            num = num*26 + ord(s[i])-ord('A')+1
        return num

if __name__=="__main__":
    a = 'AZ'
    print Solution().titleToNumber(a)

"""
In Excel, the range is A~Z, AA~ZZ, AAA~ZZZ. So the problem will be 26-base convert
problem, just notice start from one, so need to plus 1.
"""