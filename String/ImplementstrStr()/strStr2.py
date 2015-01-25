#!/usr/bin/python

"""
Implement strStr() 

Implement strStr().

Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle: return 0
        if not haystack: return -1
        m, n, j = len(haystack), len(needle), -1
        match = self.KMP(needle)
        for i in xrange(m):
            while j>=0 and haystack[i]!=needle[j+1]: j = match[j]
            if haystack[i] == needle[j+1]: j += 1
            if j == n-1: return i-n+1
        return -1

    def KMP(self, s):
        n, j = len(s), -1
        match = [-1] * n
        for i in xrange(1,n):
            while j>=0 and s[i]!=s[j+1]: j = match[j]
            if s[i] == s[j+1]: j += 1
            match[i] = j
        return match

if __name__=="__main__":
    s = 'This is a simple string'
    sub = 'simple'
    print Solution().strStr(s,sub)
 
"""
KMP algorithm. Complexity is O(n).
Reference:
http://www.matrix67.com/blog/archives/115
"""

