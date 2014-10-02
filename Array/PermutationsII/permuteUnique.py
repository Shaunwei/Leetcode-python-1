#!/usr/bin/python

"""
Permutations II  

Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        numLen = len(num)
        if numLen == 0: return []
        if numLen == 1: return [num]
        num.sort()
        result = []
        prevNum = None
        for i in xrange(numLen):
            if num[i] == prevNum: continue
            prevNum = num[i]
            for j in self.permuteUnique(num[:i] + num[i+1:]):
                result.append([num[i]] + j)
        return result

if __name__=="__main__":
    s = [1,1,2] 
    print Solution().permuteUnique(s)

"""
The idea of permutation problem, except it need to remove
duplicate. 
"""