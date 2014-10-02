#!/usr/bin/python

"""
Wildcard Matching 

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        slen, plen = len(s), len(p)
        pPoint = sPoint = match = 0 
        star = -1
        while sPoint < slen:
            if pPoint < plen and (p[pPoint]=='?' or p[pPoint]==s[sPoint]):
                sPoint, pPoint = sPoint+1, pPoint+1
                continue
            if pPoint < plen and p[pPoint]=='*':
                star, pPoint, match = pPoint, pPoint+1, sPoint
                continue
            if star != -1:
                pPoint, match, sPoint = star+1, match+1, match
                continue
            return False
        while pPoint < plen and p[pPoint]=='*':
            pPoint += 1
        return pPoint == plen

if __name__=="__main__":
    s1 = ["aa","aa","aaa","aa","aa","ab","aab"]
    s2 = ["a","aa","aa","*","a*","?*","c*a*b"]
    for i in xrange(len(s1)):
        print Solution().isMatch(s1[i],s2[i])
 
"""
For each element in s
If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
If not match, then we check if there is a * previously showed up,
       if there is no *,  return false;
       if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

e.g.

abed
?b*d**

a=?, go on, b=b, go on,
e=*, save * position star=3, save s position ss = 3, p++
e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
d=d, go on, meet the end.
check the rest element in p, if all are *, true, else false;

Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".
"""

