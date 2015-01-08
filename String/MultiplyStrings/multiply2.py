#!/usr/bin/python

"""
Multiply Strings  

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if not num1 or not num2: return '0'
        num1, num2 = num1[::-1], num2[::-1]
        result = ['0' for i in xrange(len(num1)+len(num2))]            
        for i in xrange(len(num1)):
            digi1 = ord(num1[i]) - ord('0'); 
            carry = 0
            for j in xrange(len(num2)):
                digi2 = ord(num2[j]) - ord('0')
                exist = ord(result[i+j]) - ord('0')
                result[i+j] = str((digi1*digi2+carry+exist)%10)
                carry = (digi1*digi2+carry+exist) / 10
            if carry > 0:
                result[i+len(num2)] = str(carry)
        result = ''.join(result)[::-1].lstrip('0')
        return result if result else '0'
    
if __name__=="__main__":
    num1 = '123'
    num2 = '456'
    print Solution().multiply(num2,num1)
    
"""
Straight forward idea. Just like the way we multiply numbers. Don't forget 
considering the carry and be careful. e.g.
  123*456,

what we usually do is:

      123
x     456
-----------
      738
     615
+   492
-----------
    56088
thus, 123*456 = 56088.

In the same way, the algorithm is:
A*B
(1)For each element B[i]
    Compute tmp = B[i]*A
    Add tmp to the previous result, note the start position. res = res"+"tmp
(2)Return result.

To be specific,
(1) char2int,     int(char-'0');
(2) int2char,     char(int+'0')
(3) Don't forget the carry in each add or multiply operation.
(4) Don't forget the carry after last operation. e.g.  82+33 = 115.
(5) Be careful with the string order and the number order.
"""
 

