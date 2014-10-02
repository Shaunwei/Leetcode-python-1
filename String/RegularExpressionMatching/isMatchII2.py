#!/usr/bin/python

"""
Regular Expression Matching 

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        return self.match(s, p, 0, 0) 

    def match(self, s, p, iS, iP):
        if iP >= len(p): return iS >= len(s) 
        if iP == len(p)-1:
            return (iS==len(s)-1) and (s[iS]==p[iP] or p[iP]=='.') 
        if iP+1<len(p) and p[iP+1]!='*':
            if iS == len(s): return False  
            if s[iS]==p[iP] or p[iP]=='.': return self.match(s,p,iS+1,iP+1) 
            else: return False 
        while iS<len(s) and iP<len(p) and (s[iS]==p[iP] or p[iP]=='.'):
            if self.match(s,p,iS,iP+2): return True 
            iS += 1
        return self.match(s,p,iS,iP+2) 

if __name__=="__main__":
    s1 = ["aa","aa","aaa","aa","aa","ab","aab","",   "ab", "aaa","a","a",  "bb", "bb"]
    s2 = ["a","aa","aa","a*",".*",".*","c*a*b","bab",".*c","a.a",".","ab*",".bab","*"]
         # T,  F,  T,    F,   T,   T,   T,     F,     F,    T,    T,  T,    F,    F
    for i in xrange(len(s1)):
        print Solution().isMatch(s1[i],s2[i])
 
"""
Note that this problem is NOT the same as Wildcard Matching.
The major difference is the meaning of  "*" in the string.
Here, "*" means 0 or more preceding element. For example, the last test case in the problem description: 
    isMatch("aab",""c*a*b")
The pattern :  "c*a*b" means,  there can be 0 or more 'c', 0 or more 'a' and one b.
e.g., "ccaab", "aab", "ccb", "b" are all valid strings for this pattern, thus the correct answer for this test case is also true (0 'c', 2 'a' and 1 'b').

This is recursive version gets Time Limit Exceeded!!
"""

