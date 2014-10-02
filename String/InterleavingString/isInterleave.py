#!/usr/bin/python

# Interleaving String 

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1+len2 != len3: return False
        match = [[0 for i in xrange(len2+1)] for j in xrange(len1+1)]
        for i in xrange(len1+1):
            for j in xrange(len2+1):
                if i>0 and match[i-1][j]==i-1+j and s1[i-1]==s3[i-1+j]:
                    match[i][j] = i + j
                if j>0 and match[i][j-1]==i+j-1 and s2[j-1]==s3[i+j-1]:
                    match[i][j] = i + j
        print match
        return match[len1][len2]==len3
         
if __name__=="__main__":
    s1,s2,s3 = "aabcc","dbbca","aadbbcbcac"#"aadbbcbccc"
    print Solution().isInterleave(s1,s2,s3)

'''
Using dynamic programming (DP).
match[i][j]=m means the front to ith charactors of s1 and the front to jth charactors of s2 can form the front to mth charactors of s3, so in the end when match[len_s1][len_s2]==len_s3 return true.
'''
