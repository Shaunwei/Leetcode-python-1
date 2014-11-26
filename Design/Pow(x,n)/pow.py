#!/usr/bin/python

"""
Pow(x, n) 

Implement pow(x, n).
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        return self.power(x,n) if n>=0 else 1.0/self.power(x,-n)

    def power(self, x, n):
        if n == 0: return 1
        half = self.power(x, n/2)
        return half*half if n%2==0 else half*half*x

if __name__=="__main__":
    x = 4.0
    n = 3
    print Solution().pow(x,n)

"""
Using binary search. Also need consider when n < 0.
Consider this way:
For compute 2^10:
2^10  = 2^4 * 2^4 *2^2
2^4 = 2^2*2^2
2^2 = 2*2
"""
