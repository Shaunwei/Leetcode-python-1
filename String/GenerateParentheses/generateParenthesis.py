#!/usr/bin/python

"""
Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.n = n
        self.result = []
        self.gen('',0,0)
        return self.result        

    def gen(self, s, leftParaNum, rightParaNum):
        if leftParaNum == rightParaNum == self.n:
            self.result.append(s); return
        if leftParaNum < self.n:
            self.gen(s+'(', leftParaNum+1,rightParaNum)
        if rightParaNum < leftParaNum <= self.n:
            self.gen(s+')', leftParaNum,rightParaNum+1)
        return
 
if __name__=="__main__":
    print Solution().generateParenthesis(3)
 
"""
The classic question from the Cracking the Code Interview. DFS is enough. 
Note that it is wrong when the number of ')' is more than '(' in the current string. e.g. ()()).
"""

