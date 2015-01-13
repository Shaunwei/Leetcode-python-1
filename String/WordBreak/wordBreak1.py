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
        segment = [True]
        for i in range(len(s)):
            segment.append(False)
            for j in range(i,-1,-1):
                if segment[j] and s[j:i+1] in dict:
                    segment[i+1] = True
                    break 
        return segment[len(s)]

if __name__=="__main__":
    string = "leetcode"
    dicts = ["leet","code"] 
    sol = Solution()
    print sol.wordBreak(string,dicts)

"""
The same DP method but in reverse way.

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