#!/usr/bin/python

"""
Container With Most Water 

Given n non-negative integers a1, a2, ..., an, where each represents 
a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container 
contains the most water.

Note: You may not slant the container.
"""

class Solution:
    # @return an integer
    def maxArea(self, height):
        l, r, maxWater = 0, len(height) - 1, -1
        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxWater
    	

if __name__=="__main__":
    height = [1,5,3,7]
    print Solution().maxArea(height)

"""
There is a greedy way to solve this problem in O(n). Use two pointers, 
one from the start and one from the end of the height vector. 
Compute the current area, move the smaller pointer to its direction, 
until two pointers meet. For example: height = [1,5,3,7]
                _
               | |
      _        | |
     | |       | |
     | |   _   | |
     | |  | |//| |
 _   | |  | |//| |
| |  | |  | |//| | 
------------------
"""