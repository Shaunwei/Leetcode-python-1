#!/usr/bin/python
"""
Palindrome Partitioning 

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

 [
   ["aa","b"],
   ["a","a","b"]
 ]
"""

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.s, self.result, self.strLen = s, [], len(s)
        self.isPali = [[False for j in xrange(self.strLen)] for i in xrange(self.strLen)]
        for j in xrange(self.strLen):
            for i in reversed(xrange(j+1)):
                if s[i]==s[j] and (j-i<=1 or self.isPali[i+1][j-1]==True):
                # True means substring from s[i](included) 
                #   to s[j](included) is palindrome
                     self.isPali[i][j] = True
        self.dfs(0,[])
        return self.result
 
    def dfs(self, start, paliStr):
        if start == self.strLen:
            self.result.append(paliStr)
            return
        # make a copy of list L and add a substring
        for end in xrange(start, self.strLen):
            if self.isPali[start][end] == True:
                self.dfs(end+1, paliStr[:]+[self.s[start:end+1]])
        
if __name__=="__main__":
    string = "aab"
    print Solution().partition(string)

"""
Dynamic programming. First use isPal to record each substring is palindrome or not. 
"isPal[i][j] == true" means a substring starts from s[i] (included) to s[j] (included) 
is a palindrome. Then use DFS.
"""
