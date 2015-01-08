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
        needleLen = len(needle)
        haystackLen = len(haystack)
        if needleLen==haystackLen and needleLen==0: return 0
        if needleLen == 0: return 0
        for i in xrange(haystackLen):
		    # make sure in boundary of needle
            if haystackLen-i+1 < needleLen: return -1
            k, j = i, 0
            while j<needleLen and k<haystackLen and needle[j]==haystack[k]:
			    k, j = k+1, j+1
			    if j == needleLen: return i
        return -1

if __name__=="__main__":
    s = 'This is a simple string'
    sub = 'simple'
    print Solution().strStr(s,sub)
 
"""
First, need to understand the problem correctly, the pointer simply means a sub string.
Second, make sure the loop does not exceed the boundaries of two strings.
This is brute force version, the better algorithm is KMP.
"""

