#!/usr/bin/python

"""
Divide Two Integers

Divide two integers without using multiplication, division and mod operator.
"""

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign, quot = 1, 0 
        if dividend < 0: sign = -sign;dividend = -dividend
        if divisor < 0: sign = -sign;divisor = -divisor
        while dividend >= divisor:
            k, tmp = 0, divisor
            while dividend >= tmp:
                quot += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return quot if sign > 0 else -quot

if __name__=="__main__":
    dend = 9; dsor = 3
    print Solution().divide(dend,dsor)

"""
Using bit operator.
Note that is the dividend < divisor as they all integer and the return 
value is also integer, the return value would be 0.  (e.g. 1/4=0)

Without using the *, /, and % operator, what we can use is +,-, and <<, >> .
<< 1 is to multiply 2,e.g. 2<<1  = 4;
>> 1 is to divide 2, e.g.   8>>1 = 4;

use << to speed up.
1. Keep  multiply 2 (<<1) to the divisor, until it is greater than the dividend. 
Store the times of shift operation.
2. if dividend > divisor, then dividend = dividend - divisor*2(<<1). 
Until dividend < original divisor. Store the result.
3. Output the result.

e.g. 15/3
3*2*2*2=24>15, 
15 - 24/2 = 3 - 12/2/2=0 < 3, end.
res = 4,        res = 4+1,   res=5
"""
