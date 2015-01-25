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
        if haystack==needle and len(needle) == 0: return 0
        if len(needle) == 0: return 0
        result = haystack.find(needle)
        return result   

if __name__=="__main__":
    s = 'This is a simple string'
    sub = 'simple'
    print Solution().strStr(s,sub)
