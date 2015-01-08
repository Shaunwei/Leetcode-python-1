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
        i, j, maxLen = 0, -1, 0
        for k in xrange(1,len(s)):
            if s[k] == s[k-1]: continue
            if j>=0 and s[j]!=s[k]:
                maxLen = max(k-i,maxLen)
                i = j + 1
            j = k - 1
        return max(len(s)-i,maxLen)

if __name__=="__main__":
    s = 'abcbbbbcccbdddadacb'#'abaac' #'eceba'
    print Solution().maxLength(s)

"""
An O(n) solution: (this is standard solutin)
the idea is to maintain a sliding window.
use two pointers, one store the previous different char index.
e.g.
index   0 1 2 3 4 
str     a b a a c 
1st run --^---^
2nd run     ^---^
"""