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
        result = []
        if k == 0:
            return result
        comb = [0] * k
        p = 0
        while p >= 0:
            comb[p] += 1
            for i in xrange(p+1, k):
                comb[i] = comb[i-1] + 1
            result.append(list(comb))
            p = k-1
            while p >= 0 and comb[p] == n - (k - 1 - p):
                p -= 1
        return result

if __name__=="__main__":
    print Solution().combine(4,3) # 4,2

"""
counting p, when p reach the maximum number k, then moving p forward.
For example, combine(5,3), when get [1,2,5], p point to poistion 3rd and 
it reach maximum number 5, then p move to position 2nd, comb[p] += 1,
so we get [1,3,4]. And when p in position 1st reach the maximum k, such as
[3,4,5], then program end.
"""

