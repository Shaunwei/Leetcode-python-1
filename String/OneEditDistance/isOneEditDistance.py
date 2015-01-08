#!/usr/bin/python

"""
One Edit Distance

Given two strings S and T, determine if they are both one edit 
distance apart.

Hint:
1. If | n - m | is greater than 1, we know immediately both are 
not one-edit distance apart.
2. It might help if you consider these cases separately, m == n and m != n.
3. Assume that m is always <= n, which greatly simplifies the conditional 
statements. If m > n, we could just simply swap S and T.
4. If m == n, it becomes finding if there is exactly one modified operation. 
If m != n, you do not have to consider the delete operation. Just consider 
the insert operation in T.
"""

class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        if len(s) > len(t): s, t = t, s
        lenS,lenT,flag,i,j = len(s),len(t),False,0,0
        if lenT - lenS > 1: return False
        while i < lenS:
            if s[i] != t[j]:
                if flag: return False
                flag = True
                if lenS < lenT: i -= 1
            i, j = i+1, j+1
        return flag or lenS < lenT

if __name__=="__main__":
    word1 = "abd"
    word2 = "abcd"
    print Solution().isOneEditDistance(word1,word2)

"""
Just two cases:
1. when s length equals t length, then no more than one char different.
2. if s length is less than t length, then there is one char in t different
from s either in the middle of s or may be append to s, such 'abc' and 'abcd'.
"""