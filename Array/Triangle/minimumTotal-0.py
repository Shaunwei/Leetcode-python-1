#!/usr/bin/python

"""
Triangle

Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
"""

class Solution:
  # @param triangle, a list of lists of integers
  # @return an integer
  def minimumTotal(self, triangle):
      rowLen = len(triangle)
      minpath = [0 for i in xrange(rowLen)]
      for r in triangle:
          mempath = minpath[:]
          for i in xrange(len(r)):
              if i == 0:
                  minpath[i] = r[i] + mempath[i]
              elif i == len(r)-1:
                  minpath[i] = r[i] + mempath[i-1]
              else:
                  minpath[i] = min(mempath[i],mempath[i-1]) + r[i]
      return min(minpath)

if __name__=="__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print Solution().minimumTotal(triangle)


"""
Top down dp.
"""

