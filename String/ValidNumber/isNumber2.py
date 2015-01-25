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
        state = 0
        for i in xrange(0,len(s)):
            state = self.nextState(state, s[i])
            if state == -1: 
                return False
        state = self.nextState(state, ' ')
        return state == 8
    
    def nextState(self, state,char):
        transititionTable = [[0,2,1,3,-1,-1], [-1,2,-1,3,-1,-1], [8,2,-1,4,5,-1], [-1,4,-1,-1,-1,-1], [8,4,-1,-1,5,-1],[-1,7,6,-1,-1,-1],[-1,7,-1,-1,-1,-1], [8,7,-1,-1,-1,-1], [8,-1,-1,-1,-1,-1]];
        return transititionTable[state][self.getSymbol(char)]
    
    def getSymbol(self, char):
        if char == ' ' or char == '\t':
            return 0
        if char.isdigit():
            return 1
        if char == '+'  or char == '-':
            return 2
        if char == '.':
            return 3
        if char == 'E' or char =='e':
            return 4
        return 5

if __name__=="__main__":
    a = ["0"] # true
    a.append(" 0.1 ") # true
    a.append("abc") # false
    a.append("1 a") # false
    a.append("2e10") # true
    for i in xrange(len(a)):
        print Solution().isNumber(a[i])

"""
This is problem about Deterministic finite automaton(DFA).

http://jelices.blogspot.com/2014/05/leetcode-python-valid-number.html

More information:
[1, Chapter 1] J. Glen Brookshear, "Theory of Computation: Formal Languages, Automata, and Complexity", Addison-Wesley.
[2, Chapters 2-3] Rajeev Motwani, Jeffrey Ullman, and John Hopcroft, "Introduction to Automata Theory, Languages, and Computation", Addison-Wesley.
"""    
