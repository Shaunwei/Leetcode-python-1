#!/usr/bin/python

"""
Longest Substring with At Most Two Distinct Characters

GGiven a string S, find the length of the longest substring 
T that contains at most two distinct characters.

For example,
Given S = "eceba",
T is "ece" which its length is 3.
"""

class Solution:
    # @return a int
    def maxLength(self, s):
        if len(s) == 0: return 0
        diffIdx, curLen, maxLen = -1, 1, 1
        maxIdx = 0 #for print maxLen substr
        for i in xrange(1,len(s)):
            if s[i] != s[i-1]:
                if diffIdx==-1 or s[i] == s[diffIdx]:
                    curLen += 1
                else: curLen = i - diffIdx
                diffIdx = i - 1
            else: curLen += 1
            if maxLen < curLen:
                maxLen = curLen
                maxIdx = i-curLen+1 #for print maxLen substr
        # return maxLen
        return s[maxIdx:maxIdx+maxLen] #for print maxLen substr

if __name__=="__main__":
    s = 'abcbbbbcccbdddadacb'#'abaac' #'eceba'
    print Solution().maxLength(s)

"""
An O(n) solution:
the idea is to maintain a sliding window.
use two pointers, one store the previous different char index.
e.g.
index   0 1 2 3 4 
str     a b a a c 
1st run --^---^
2nd run     ^---^
"""