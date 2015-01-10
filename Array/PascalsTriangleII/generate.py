#!/usr/bin/python

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
    	if rowIndex == 0: return [1]
    	if rowIndex == 1: return [1,1]
    	triangle = [1]
    	for i in range(1,rowIndex/2+1):
    		triangle.append(triangle[i-1]*(rowIndex+1-i)/i)
    	if rowIndex % 2 == 1:
    		triangle += triangle[::-1]
    	else:
    		n = len(triangle)
    		triangle += triangle[n-2::-1]
    	return triangle

if __name__=="__main__":
    numRows = 11
    print Solution().getRow(numRows)

"""
This can be solved in according to the formula to generate 
the kth element in nth row of Pascal's Triangle:

r(k) = r(k-1) * (n+1-k)/k,

where r(k) is the kth element of nth row. The formula just 
use the previous element to get the new one. The start point is 1.
Once get the formula, it is easy to generate the nth row.
"""