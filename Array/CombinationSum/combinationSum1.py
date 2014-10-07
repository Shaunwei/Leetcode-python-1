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
        result, lst = [], []
        if len(candidates) == 0: return result
        candidates.sort()
        self.dfs(candidates,target,result,lst,0)
        return result

    def dfs(self, candidates, target, result, lst, index):
        if target < 0: return
        else:
            if target == 0: result.append(list(lst))
            else:
                while index<len(candidates) and target-candidates[index]>=0:
                    lst.append(candidates[index])
                    self.dfs(candidates,target-candidates[index],result,lst,index)
                    index += 1
                    lst.pop()

if __name__=="__main__":
    candidates = [8,7,4,3] # [2,3,6,7] 
    target = 11 # 7
    print Solution().combinationSum(candidates,target)

"""
Using DFS:
The idea is to scan from the first to the last element from the ordered array. 
check every possible combination of these numbers(multiple times for a single element).
The end condition of the dfs function is
1. the target ==0 , print list, return
2. the target < 0 return
3. start position >= array size return
otherwise, from for each element in the array, dfs(start, target-element value);
"""


