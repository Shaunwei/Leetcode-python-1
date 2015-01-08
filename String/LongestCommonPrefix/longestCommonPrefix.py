#!/usr/bin/python

"""
Longest Common Prefix   

Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        strslen = len(strs)
        if strslen == 0: return ''
        if strslen == 1: return strs[0]
        lens = [len(i) for i in strs]
        compref = ''
        for i in xrange(min(lens)): 
            strtmp = strs[0][i]
            for j in xrange(1,strslen):
                if strs[j][i] != strtmp: return compref
            compref += strtmp
        return compref
            
if __name__=="__main__":
    strs = ['abcd','abc','abd','abbc','ab']
    print Solution().longestCommonPrefix(strs)
 
"""
The idea is scan from the first character, if it is same for all the strings, go to the 
next character.Return the string until meet the different character.
"""

