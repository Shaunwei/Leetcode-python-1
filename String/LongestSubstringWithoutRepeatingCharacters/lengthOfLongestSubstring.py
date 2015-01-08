#!/usr/bin/python

"""
Longest Substring Without Repeating Characters 

Given a string, find the length of the longest substring without 
repeating characters. For example, the longest substring without 
repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxlen, substr, rear = 0, '', 0
        for front in xrange(len(s)):
            if s[front] not in substr: substr += s[front]
            else:
                maxlen = max(maxlen, len(substr))
                while s[rear] != s[front]: rear += 1
                rear += 1
                substr = s[rear:front+1]
        return max(maxlen, len(substr))      

if __name__=="__main__":
    S="qpxrjxkltzyx" #"abcabcbb"
    print Solution().lengthOfLongestSubstring(S)
 
"""
Use two pointer scan string from left to right, when front pointer 
meet reapt character, we get a max substring length; then start from 
rear point + 1 to scan over till the end.
Example: 
index   0 1 2 3 4 5 6 7 8 9 10 11 
str     q p x r j x k l t z y  x
1st run ^ ------> ^
2nd run       ^ -------------> ^
3rd run             ^ -------> ^    
"""

