#!/usr/bin/python
"""
ZigZag Conversion 

The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a 
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given 
a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution:
    # @param s, a string
    # @return an integer
    def convert(self, s, nRows):
        if s == None: return None
        if nRows <= 1: return s
        sz = len(s)
        sb = ''
        for i in xrange(nRows):
            j=i
            while j < sz:
                sb += s[j]
                #define new int k and save the old value in j for next loop
                if i%(nRows-1) != 0:
                    k = j + (nRows-1-i)*2 
                    if k < sz: sb += s[k]  #must check k<sz; may be exceed string length.
                j += 2*(nRows-1)
        return sb
			

if __name__=="__main__":
    s = "PAYPALISHIRING"
    print Solution().convert(s,3)
    print Solution().convert(s,4)
