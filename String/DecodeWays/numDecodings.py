#!/usr/bin/python
"""
Decode Ways 

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == '' or s[0] == '0':return 0
        ways = [1,1]
        for i in xrange(2,len(s)+1):
            if 10 <= int(s[i-2:i]) <= 26 and '1' <= s[i-1] <= '9':
                ways.append(ways[i-1]+ways[i-2])
            elif 10 <= int(s[i-2:i]) <= 26:
                ways.append(ways[i-2])
            elif '1' <= s[i-1] <= '9':
                ways.append(ways[i-1])
            else: # s[i] == '0'
                return 0
        return ways[len(s)]

if __name__=="__main__":
    s = "12"
    print Solution().numDecodings(s)

'''
Using one dimension DP. First we need look at the current value and previous value, 
also need mind the 0 case, such as "10", "101" which can only count one decode way. 
ways[N]=M means the previous N charactors of string s have M decode ways.
'''
