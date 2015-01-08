#!/usr/bin/python

"""
Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return a string
    def intToRoman(self, num):
        res, ran, roman = '', 1000, ['I','V','X','L','C','D','M']
        for i in xrange(6,-1,-2):
            digi = num / ran
            if digi != 0:
                if digi <= 3: res += roman[i]*digi
                elif digi == 4: res += roman[i]+roman[i+1]
                elif digi == 5: res += roman[i+1]
                elif digi <= 8: res += (roman[i+1]+roman[i]*(digi-5))
                elif digi == 9: res += roman[i]+roman[i+2]
            num, ran = num%ran, ran/10 
        return res

if __name__=="__main__":
    num = 8 #14
    print Solution().intToRoman(num)

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
Need handle every digit in the range of roman number,
1<= digit <=3
digit = 4
digit = 5
5 < digit <= 8
digit = 9
"""

