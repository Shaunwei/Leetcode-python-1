#!/usr/bin/python

# Palindrome Partitioning II 

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. 


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        strLen = len(s)
        isPali = [[False for j in xrange(strLen)] for i in xrange(strLen)]
        minPaNum = [i+1 for i in xrange(strLen)]
        for j in xrange(strLen):
            for i in reversed(xrange(j+1)):
                if s[i]==s[j] and (j-i<=1 or isPali[i+1][j-1]==True):
                # True means substring from s[i](included) 
                #   to s[j](included) is palindrome
                     isPali[i][j] = True
                     minPaNum[j] = min(minPaNum[j],minPaNum[i-1]+1) if i>0 else min(minPaNum[j],1) # i == 0
        return minPaNum[strLen-1]-1

        
if __name__=="__main__":
    string = "aab"
    print Solution().minCut(string)

'''
Dynamic programming. Use "isPal" to record whether a substring is a palindrome or not, "isPal[i][j] == true" means a substring starts from s[i] (includsive) to s[j] (inclusive) is a palindrome. Use "minPalNum" to record the minimum number of palindromes within a substring start from s[0], "minPalNum[i] == 3" means a substring starts from s[0] (included) to s[i] (included) has 3 palindromes and 3 is the minimum number. When we meet a "isPal[i][j] == true" case, we update minPalNum. Finally the result is minPalNum[lenS] - 1.
'''
