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
        length = len(A)
        S = [0 for i in xrange(length)]
        S[0] = A[0]
        for i in xrange(1, length):
            if S[i-1] > 0:
                S[i] = S[i-1] + A[i]
            else:
                S[i] = A[i]
        return max(S)

if __name__=="__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(arr)


"""
divide and conquer:
S[i] store the result of subarray with A[i] as last added value. 
"""
