#!/usr/bin/python

"""
Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 0
        for i in reversed(xrange(len(digits))):
            digits[i] = digits[i] + 1 + carry if i == len(digits) - 1 else digits[i] + carry
            carry = 1 if digits[i] == 10 else 0
            if digits[i] == 10: digits[i] = 0
        return [1] + digits if carry == 1 else digits
    	

if __name__=="__main__":
    digits = [9,9,9,9]
    print Solution().plusOne(digits)



