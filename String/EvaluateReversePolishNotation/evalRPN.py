#!/usr/bin/python

# Evaluate Reverse Polish Notation

#Evaluate the value of an arithmetic expression in Reverse Polish Notation.

#Valid operators are +, -, *, /. Each operand may be an integer or another #expression. 

#Some examples:

#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        #import operator
        #ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div }
        result = 0
        nums = []
        while len(tokens) > 0:
            c = tokens.pop(0)
            try:
                b = int(c)
                nums.append(b)
                if not tokens:
                    return b
            except ValueError:
		if len(nums) > 1:
                    a = nums.pop()
                    b = nums.pop()
                    #result = ops[c](b,a)
		    if c=="+":
                        result = b + a
                    if c=="-":
                        result = b - a
                    if c=="*":
                        result = b * a
                    if c=="/":
                        result = int(float(b) / a)
                    nums.append(result)
		    
        return result

if __name__=="__main__":
    sol = Solution()  
    str1 = ["2", "1", "+", "3", "*"] # 9 
    str2 = ["4", "13", "5", "/", "+"] # 6
    str3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
    print str1,sol.evalRPN(str1)
    print str2,sol.evalRPN(str2)
    print str3,sol.evalRPN(str3)
