#!/usr/bin/python

"""
Roman to Integer 

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        res, roman = 0, {'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000}
        for i in xrange(len(s)):
            if i>0 and roman[s[i]] > roman[s[i-1]]:
                res += roman[s[i]] - roman[s[i-1]]*2
            else: res += roman[s[i]]
        return res

if __name__=="__main__":
    s = 'IX'
    print Solution().romanToInt(s)

"""
Roman number rules(see wiki):
Forms:
I   1
V   5
X   10
L   50
C   100
D   500
M   1000

Idea: 
scan string from front to end; if current value greater than previous, then
current subtracts previous, such as IV = V - I = 5-1 = 4;
otherwise, accumulate the current value to result.
"""

