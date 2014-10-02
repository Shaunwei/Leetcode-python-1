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
        result = []
        self.getPerm(num,0,len(num)-1,result)
        return result

    def getPerm(self, num, k, n, result):
        if k == n: result.append(list(num))
        else:
            for i in xrange(k,n+1):
                if self.isDupli(num,k,i):
                    continue
                num[k],num[i] = num[i],num[k]
                self.getPerm(num,k+1,n,result)
                num[k],num[i] = num[i],num[k]

    def isDupli(self, num, k, i):
        for j in xrange(k,i):
            if num[j] == num[i]: return True
        return False

if __name__=="__main__":
    s = [1,1,2] 
    print Solution().permuteUnique(s)

"""
The idea of permutation problem, except it need to remove
duplicate. 
"""