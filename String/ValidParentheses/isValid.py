#!/usr/bin/python

"""
Valid Parentheses 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        if s == '': return True
        stack = []
        for i in s:
            if i in '([{': stack.append(i)
            else:
                if not stack: return False
                if i==')' and stack[-1]!='(': return False
                if i==']' and stack[-1]!='[': return False
                if i=='}' and stack[-1]!='{': return False
                stack.pop()
        return not stack

if __name__=="__main__":
    s =  "([)]" # '()[]{}' #
    print Solution().isValid(s)
 
"""
Use a stack to store the chars, scan from the 1st to the last char in string s.
( [ { are free to push in the stack.
When meets ) if stack top is (, then pop (.
When meets ] if stack top is [, then pop [.
When meets } if stack top is {, then pop {.
Otherwise return false.
"""

