#!/usr/bin/python

"""
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 3: return n
        f1, f2 = 1, 2
        for i in xrange(3,n+1):
            f2 = f1 + f2
            f1 = f2 - f1
        return f2

if __name__=="__main__":
    n = 5
    print Solution().climbStairs(n)

"""
The idea is a Fibonacci number. f(n) = f(n-1) + f(n-2).
The nth stairs is from either n-1th the stair or the n-2th stair. 
"""
