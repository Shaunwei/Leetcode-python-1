#!/usr/bin/python

"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest 
valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        slen, stack, maxpara = len(s), [(-1,')')], 0
        for i in xrange(slen):
            if s[i] == ')' and stack[-1][1] == '(': #stack[-1] means stack top
                stack.pop()
                maxpara = max(maxpara,i-stack[-1][0])
            else:
                stack.append((i,s[i]))
        return maxpara

if __name__=="__main__":
    para = ')()())'
    print Solution().longestValidParentheses(para)
 
"""
Use a stack to record left paren, right parenthese and index. If current paren is ')' and 
stack top is '(' then pop up and update maxLen.
"""