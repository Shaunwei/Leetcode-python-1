#!/usr/bin/python

"""
Subsets II  

Given a collection of integers that might contain duplicates, S, 
return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
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
        i = step
        while i < len(s):
          subarr.append(s[i])
          result.append(list(subarr))
          if i < len(s)-1: self.getSubarr(s,i+1,result,subarr)
          subarr.pop()
          while i < len(s)-1 and s[i] == s[i+1]: i += 1
          i += 1

if __name__=="__main__":
    s = [1,2,2] 
    print Solution().subsets(s)

"""
Same as Subsets problem, only diffferent is to remove the duplicate.
"""