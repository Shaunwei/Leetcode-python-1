#!/usr/bin/python

"""
Combination Sum 

Given a set of candidate numbers (C) and a target number (T), find all 
unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,..., ak) must be in non-descending order. 
(ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        dp = {}; dp[0] = [[]]
        for i in xrange(1, target + 1):
            dp[i] = [] 
            for num in candidates:
                # dp[i-num] means it's not empty
                if i >= num: # and dp[i-num]: 
                    for L in dp[i-num]:
                        tmp = sorted(L + [num])
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
        # return [] is possible, e.g. candidates = [2], target = 1 
        return dp[target] if target in dp else []

if __name__=="__main__":
    candidates = [2,3,6,7] 
    target = 7
    print Solution().combinationSum(candidates,target)

"""
Using DP:
figure out solution set when target=1,2,3...N; the late outcome
result based on the previous.
"""


