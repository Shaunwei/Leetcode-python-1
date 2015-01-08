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
        dp = [0,1,2]
        for i in xrange(3,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]

if __name__=="__main__":
    n = 5
    print Solution().climbStairs(n)

"""
Using one dimension dp.
"""
