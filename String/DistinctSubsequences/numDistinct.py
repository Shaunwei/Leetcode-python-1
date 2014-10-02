#!/usr/bin/python

# Distinct Subsequences 

# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.


class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        lenS = len(S)
        lenT = len(T)
        match = [[0 for i in xrange(lenT+1)] for j in xrange(lenS+1)]
		# empty string is a subsequence of any string
        for i in xrange(lenS+1):
            match[i][0] = 1
        for i in xrange(1,lenS+1):
            for j in xrange(1,min(i+1,lenT+1)):
                match[i][j] = match[i-1][j-1] + match[i-1][j] if S[i-1]==T[j-1] else match[i-1][j]
        return match[lenS][lenT]
 
        
if __name__=="__main__":
    S = "ccc"#"rabbbit"
    T = "c"#"rabbit"
    print Solution().numDistinct(S,T)

'''
The idea is using dynamic programming (DP).
The key is to find the recursive relation. We can think in this way: consider the original string length is j, substring length is i. All we need to do is to count the number when i length substring appear in the original j length string. Let the count to be t[i][j], if the last charactor of original string is not eaqual to last charactor of substring, which means appear count number of i length substring will in the j-1 length original string that is t[i][j]=t[i][j-1]. If both last charactors is same, then we need count the last charactor as addition that is t[i][j]=t[i][j-1]+t[i-1][j-1].
'''
