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
        nums = [' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result = []
        self.generate(nums,digits,0,'',result)
        return result

    def generate(self,nums,digits,deep,res,result):
        if deep == len(digits):result.append(res);return
        curdg = ord(digits[deep]) - ord('0')
        for i in xrange(len(nums[curdg])):
            res += nums[curdg][i]
            self.generate(nums,digits,deep+1,res,result)
            res = res[:-1]      

if __name__=="__main__":
    s = '23'
    print Solution().letterCombinations(s)
 
"""
This is a simple problem, we can use the DFS to solve it.
"""

