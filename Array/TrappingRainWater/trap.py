#!/usr/bin/python

"""
Trapping Rain Water 

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it 
is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        if n < 2: return 0    
        l, r, vol= [0]*n, [0]*n, 0
        l[0] = r[n-1] = 0 
        for i in xrange(1,n):
            l[i] = max(l[i-1],A[i-1])         
        for i in reversed(xrange(n-1)):
            r[i] = max(r[i+1],A[i+1])
        for i in xrange(n):
            if min(l[i],r[i]) - A[i] > 0:
                vol += min(l[i],r[i])-A[i]
        return vol
    	
if __name__=="__main__":
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
    print Solution().trap(A)


"""
An O(n) solution idea:
For each bar, the water itself can trap depends on the 
max height on its left and right, that means for each 
coordinate need to check its left and right max value, 
then substract from it to get the volume.
Steps as follows:
1. Scan from left to right of array, for each coordinate, 
find the maximum left value.
2. Scan from right to left of array, for each coordinate,
find the maximum value.
3. Scan array again to accumulate the volume and get the result. 
"""
