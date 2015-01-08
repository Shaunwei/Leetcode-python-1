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
        result = []
        if len(S) == 0: return result
        result.append([])
        S.sort()
        self.getSubarr(S,0,result,[])
        return result

    def getSubarr(self, s, step, result, subarr):
        for i in xrange(step,len(s)):
            subarr.append(s[i])
            result.append(list(subarr))
            # if i < len(s)-1: self.getSubarr(s,i+1,result,subarr)
            self.getSubarr(s,i+1,result,subarr)
            subarr.pop()

if __name__=="__main__":
    s = [1,2,3] 
    print Solution().subsets(s)

"""
Use DFS.
"""