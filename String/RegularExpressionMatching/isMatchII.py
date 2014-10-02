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
        res = [[False for i in xrange(len(p)+1)] for j in xrange(len(s)+1)]
        res[0][0] = True
        for i in xrange(1,len(p)+1):
            if p[i-1] == '*':
                if i >= 2: res[0][i] = res[0][i-2]
        for i in xrange(1,len(s)+1):
            for j in xrange(1,len(p)+1):
                if p[j-1] == '.': res[i][j] = res[i-1][j-1]
                elif p[j-1] == '*':
                    res[i][j] = res[i][j-1] or res[i][j-2] or \
(res[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else: res[i][j] = res[i-1][j-1] and s[i-1]==p[j-1]
        return res[len(s)][len(p)]

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

This is DP version, more efficient.
"""

