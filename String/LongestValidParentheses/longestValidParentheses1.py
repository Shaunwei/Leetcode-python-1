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
        stack, last, maxpara = [], -1, 0
        for i in xrange(len(s)):
            if s[i] == '(': stack.append(i)
            else:
                if not stack: last = i
                else:
                    stack.pop()
                    if not stack: maxpara = max(maxpara,i-last)
                    else:  maxpara = max(maxpara,i-stack[-1])
        return maxpara

if __name__=="__main__":
    para = ')()())'
    print Solution().longestValidParentheses(para)
 
"""
Stack is used to stored the character.
If current character is '(', push into the stack.
If current character is ')',
    Case 1: the stack is empty, reset previous result to zero. Here we renew a pointer to store the earliest index.
    Case 2: the stack is not empty, pop the top element. if the top element is '(' , (which means a () pair is found), 
            then if the poped stack is empty, (which means the previous pairs should be added.), 
            len = current pos - previous pos +1; If the poped stack is not empty, len = current pos- index of stack top element.
"""