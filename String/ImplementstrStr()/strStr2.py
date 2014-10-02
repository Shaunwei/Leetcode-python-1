#!/usr/bin/python

"""
Implement strStr() 

Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if haystack==needle and len(needle) == 0: return ''
        if len(needle) == 0: return haystack
        result = haystack.find(needle)
        return haystack[result:] if result !=-1 else None     

if __name__=="__main__":
    s = 'This is a simple string'
    sub = 'simple'
    print Solution().strStr(s,sub)
 
"""
First, need to understand the problem correctly, the pointer simply means a sub string.
Second, make sure the loop does not exceed the boundaries of two strings.
"""
