#!/usr/bin/python

"""
Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip();
        slen = len(s)
        if not s: return False
        i = 0
        e = False # check if 'e' exists
        dot = False # check if '.' exists
        digit = False
        while i <= len(s)-1:
            if i==0: # a number can start with +, -, .
                if s[i]<'0' or s[i]>'9': # if is 0-9 continue
                    if s[i]=='+' or s[i]=='-' or s[i]=='.':
                        if slen==1: return False # only +, - , . is not a number
                        if s[i]=='.': dot = True
                    else: return False
                else: digit = True 
                i += 1
                continue
            if i > 0:
                if s[i] in ('e','E'): # e cannot follow +,-
                    if e==False and s[i-1]!='+' and s[i-1]!='-' and digit and i!=slen-1:
                        e = True
                    else: return False
                elif s[i] in ('+','-'): # +/- can only occur before e
                    if s[i-1]=='e' or s[i-1]=='E': pass
                    else: return False
                elif s[i] == '.': # . can only occur once and cannot occure after e
                    if dot==False and e==False: dot = True
                    else: return False
                else:  # only 0-9 can be valid numbers
                    if s[i]<'0' or s[i]>'9': return False
                    else: digit = True
                i += 1
                continue   
        #last digit can only be 0-9, or ., when it is . there is no . and e before
        if s[slen-1]>='0' and s[slen-1]<='9': return True
        if s[slen-1]=='.' and not dot and not e and s[slen-2]>='0' and s[slen-2]<='9':return True
        return False

if __name__=="__main__":
    a = ["0"] # true
    a.append(" 0.1 ") # true
    a.append("abc") # false
    a.append("1 a") # false
    a.append("2e10") # true
    a.append(".") # false
    for i in xrange(len(a)):
        print Solution().isNumber(a[i])

"""
The problem is about Deterministic finite automaton(DFA).

But this solution is not using DFA.
Here are some considerations:
(1)  " . ":   "1."  true,   "1.e2" true, ".3" true.
(2) " e ":   ".e1" false,  "1e.1" false, "1e1.1" false, "2.3e" false.
(3) "+/-":  "+1.e+5" true.
"""

