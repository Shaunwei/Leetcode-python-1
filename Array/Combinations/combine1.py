#!/usr/bin/python

"""
Combinations  

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
         return self.comb(range(1,n+1), k)
         
    def comb(self, alist, k):
        result = []
        alen = len(alist)
        if k <= 0 or alen < k:
            return result
        for i in xrange(alen):
            if k == 1:
                result.append(list((alist[i],)))
            else:
                for j in self.comb(alist[i+1:], k-1):
                    result.append([alist[i]] + j)
        return result

if __name__=="__main__":
    print Solution().combine(4,3) # 4,2

"""
using DFS.
"""

