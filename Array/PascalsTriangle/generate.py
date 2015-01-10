#!/usr/bin/python

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if numRows == 0: return []
    	if numRows == 1: return [[1]]
    	if numRows == 2: return [[1], [1,1]]
    	triangle = [[1], [1,1]]
    	for i in range(numRows-2):
    		arr = [1]
    		for j in range(len(triangle[i+1])-1):
    			arr.append(triangle[i+1][j]+triangle[i+1][j+1])
    		arr.append(1)
    		triangle.append(arr)
    	return triangle

if __name__=="__main__":
    numRows = 5
    print Solution().generate(numRows)
