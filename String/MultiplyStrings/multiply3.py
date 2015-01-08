#!/usr/bin/python

"""
Multiply Strings  

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if not num1 or not num2: return ''
        if num1[0]=='0' or num2[0]=='0': return '0'
        len1, len2, num, res = len(num1), len(num2), 0, ''
        for i in reversed(xrange(1,len1+len2+1)):
            for j in reversed(xrange(1,min(i-1,len1)+1)):
                if i-j <= len2:
                    num += int(num1[j-1]) * int(num2[i-1-j])
            if i!=1 or num>0: res += str(num%10)
            num /= 10
        return res[::-1] 
    
if __name__=="__main__":
    num1 = '123'
    num2 = '456'
    print Solution().multiply(num2,num1)