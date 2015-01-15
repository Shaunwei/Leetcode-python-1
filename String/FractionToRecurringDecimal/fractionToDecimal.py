#!/usr/bin/python

"""
Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0: return '0'
        if denominator==0: return ''
        ans, dic = '', {}
        if (numerator<0) ^ (denominator<0): ans += '-'
        num, den = abs(numerator), abs(denominator)
        res = num/den; ans += str(res)
        rem = (num % den) * 10
        if rem == 0: return ans
        ans += '.'
        while rem != 0:
            if rem in dic:
                bk = dic[rem]
                ans = ans[:bk]+'('+ans[bk:len(ans)]+')'
                return ans
            dic[rem], res = len(ans), rem/den
            rem = (rem % den) * 10
            ans += str(res)
        return ans

if __name__=="__main__":
    a = -1 #455
    b = 6 #38
    print Solution().fractionToDecimal(a,b)

"""
The key insight here is to notice that once the remainder starts repeating, 
so does the divided result.

You will need a hash table that maps from the remainder to its position of the fractional part. 
Once you found a repeating remainder, you may enclose the reoccurring fractional part with 
parentheses by consulting the position from the table.

The remainder could be zero while doing the division. That means there is no repeating fractional 
part and you should stop right away.

Just like the question Divide Two Integers, be wary of edge case such as negative fractions and 
nasty extreme case such as -2147483648 / -1.

e.g.
    0.16 
   ______ 
6 ) 1.00
    0
    _____ 
    1 0       <-- Remainder=1, mark 1 as seen at position=0.
    - 6
    _____
      40      <-- Remainder=4, mark 4 as seen at position=1.
    - 36 
    _____
       4      <-- Remainder=4 was seen before at position=1, 
                  so the fractional part which is 16 starts repeating at position=1 => 1(6).
"""