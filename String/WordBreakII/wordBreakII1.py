#!/usr/bin/python

# Word Break II 

# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].  

# Very pythonic version solution
# from __future__ import print_function
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.res = []
        self.dfs(s, dict, '')
        return self.res
        
    def check(self, s, dict):  # work break part 
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
        
    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0: self.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:],dict,stringlist+' '+s[:i])

if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, dict))
    s = 'aaaaaaa'
    dict = ["aaaa", "aaa"]
    print(Solution().wordBreak(s, dict))
    s='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    dict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(s, dict))

"""
This problem is some extension of the word break problem, so the solution is 
based on the discussion in Word Break. Use Word Break result to get the break point index,
then use DFS to store the break result.
"""