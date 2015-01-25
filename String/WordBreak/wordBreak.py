#!/usr/bin/python
"""
Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented 
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".  
"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        A = [False] * n
        i = n-1
        while i >= 0:
            if s[i:n] in dict: A[i] = True
            else:
                for j in xrange(i+1, n):
                    if A[j] and s[i:j] in dict:
                        A[i] = True
                        break
            i -= 1
        return A[0]

if __name__=="__main__":
    string = "leetcode"
    dicts = ["leet","code"] 
    sol = Solution()
    print sol.wordBreak(string,dicts)

"""
We solve this problem using DP
Define a boolean array A[0..n-1], where
A[i] = True, means s[i..n-1] can be segmented into words
------------------------------------
The recursive formula is:
A[i] = True, if there exists j>i (s[i..n-1] = s[i..j-1] + s[j..n-1])
           such that s[i..j-1] is a word and A[j] = True
or A[i] = True, if s[i..n-1] is a word
------------------------------------
We fill A-table from i=n-1 to n
"""