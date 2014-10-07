#!/usr/bin/python

"""
Combination Sum II 

Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. 
(ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result, lst = [], []
        if len(candidates) == 0: return result
        candidates.sort()
        self.dfs(candidates,target,result,lst,0)
        return result

    def dfs(self, candidates, target, result, lst, start):
        if target < 0: return
        else:
            if target == 0: result.append(list(lst))
            else:
                pre = -1
                for i in xrange(start,len(candidates)):
                    if candidates[i] != pre:
                        lst.append(candidates[i])
                        self.dfs(candidates,target-candidates[i],result,lst,i+1)
                        pre = candidates[i]
                        lst.pop()

if __name__=="__main__":
    candidates = [10,1,2,7,6,1,5] 
    target = 8
    print Solution().combinationSum2(candidates,target)

"""
Using DFS:
The only difference between this problem and the previous one is each element 
can be used at most once.
We can change the recursive step to handle this.
"""


