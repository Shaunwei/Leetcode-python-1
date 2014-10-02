#!/usr/bin/python

"""
Maximum Subarray 

Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
      maxv, summ = -10**10, 0
      for i in xrange(len(A)):
        summ = summ+A[i] if summ>0 else A[i]
        maxv = max(summ,maxv)
      return maxv

if __name__=="__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(arr)


"""
Analysis:
Classic DP problem.

We can think this problem as this: if the previous sum are +, 
which is then useful for the current element, or if it is -, 
why not start the sub array from current element? We can use 
an int to store the max sum we have got, just scan the whole array, 
the result is easily found.
"""
