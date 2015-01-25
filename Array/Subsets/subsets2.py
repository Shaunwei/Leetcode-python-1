#!/usr/bin/python

"""
Subsets 

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S: return [[]]
        S.sort()
        subset = self.subsets(S[1:])
        return subset + [[S[0]]+elem for elem in subset]

if __name__=="__main__":
    s = [1,2,3] 
    print Solution().subsets(s)

"""
Use DFS.
"""