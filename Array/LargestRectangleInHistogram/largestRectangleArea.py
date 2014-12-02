#!/usr/bin/python

"""
Largest Rectangle in Histogram  

Given n non-negative integers representing the histogram's bar 
height where the width of each bar is 1, find the area of largest 
rectangle in the histogram.
          6
       5  __
       __|  |
      |  |  |   3
 2    |  |  |2  __
 __ 1 |  |  |__|  |
|  |__|  |  |  |  |
|__|__|__|__|__|__|

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
          6
       5  __
       __|__|
      |//|//|   3
 2    |//|//|2  __
 __ 1 |//|//|__|  |
|  |__|//|//|  |  |
|__|__|//|//|__|__|

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        i, maxArea, st, h = 0, 0, [], height+[0]
        while i < len(h):
            if not st or h[st[-1]] <= h[i]:
                st.append(i); i += 1
            else:
                maxArea = max(maxArea,h[st.pop()]*(i if not st else i-st[-1]-1))
        return maxArea
    	
if __name__=="__main__":
    A = [2,1,5,6,2,3]
    print Solution().largestRectangleArea(A)


"""
An O(n) solution idea:
For each bar, use a stack to store its index by ascending height. 
If meet the current index(i) bar height less than the top of stack index
bar height, then pop the stack to compute the area by height * width:
h[stack.pop()] * i - stack.top() - 1; and if stack is empty just:
h[stack.pop()] * i.
Notice that, we need add a dummy 0 to end of stack to make sure all height
can be pop.
"""
