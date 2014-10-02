#!/usr/bin/python

"""
Permutations 

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        numLen = len(num)
        if numLen == 0: return []
        if numLen == 1: return [num]
        result = []
        for i in xrange(numLen):
            for j in self.permute(num[0:i] + num[i+1:]):
                result.append([num[i]] + j)
        return result

if __name__=="__main__":
    s = [1,2,3] 
    print Solution().permute(s)
