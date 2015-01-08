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
        S.sort()
        result = []
        self.getSubarr(S,0,result,[])
        return result
    
    def getSubarr(self, S, index, result, subarr):
        if index == len(S):
            result.append(list(subarr))
        else:
            self.getSubarr(S,index+1,result,subarr)
            subarr.append(S[index])
            self.getSubarr(S,index+1,result,subarr)
            subarr.pop()

if __name__=="__main__":
    s = [1,2,3] 
    print Solution().subsets(s)

"""
Use DFS.
"""