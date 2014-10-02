#!/usr/bin/python

"""
Letter Combinations of a Phone Number  

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
     # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits: return ['']
        nums =  {'0':' ','1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',\
'7':'pqrs','8':'tuv', '9':'wxyz'}
        result = []
        self.dfsgen(digits,'',nums,result)
        return result

    def dfsgen(self,digits,res,nums,result):
        if not digits: result.append(res)
        else:
            chars = nums[digits[0]]
            for i in chars:
                self.dfsgen(digits[1:],res+i,nums,result)

if __name__=="__main__":
    s = '23'
    print Solution().letterCombinations(s)
 
"""
This is a simple problem, we can use the DFS to solve it.
"""

