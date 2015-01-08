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
        S.sort()
        result = []
        self.getSubarr(S,0,result,[])
        return result
    
    def getSubarr(self, S, index, result, subarr):
        if index == len(S):
            result.append(list(subarr))
        else:
            i = index
            while i<len(S) and S[i]==S[index]: i += 1
            self.getSubarr(S,i,result,subarr)
            subarr.append(S[index])
            self.getSubarr(S,index+1,result,subarr)
            subarr.pop()

if __name__=="__main__":
    s = [1,2,2] 
    print Solution().subsets(s)

"""
Same as Subsets problem, only diffferent is to remove the duplicate.
"""