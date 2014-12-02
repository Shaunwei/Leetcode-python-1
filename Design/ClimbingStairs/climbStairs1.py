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
        dp, i = [0,1,2], 3
        while i <= n:
            dp.append(dp[i-1]+dp[i-2])
            i += 1
        return dp[n]

if __name__=="__main__":
    n = 5
    print Solution().climbStairs(n)

"""
Using one dimension dp.
"""
