#!/usr/bin/python

"""
Search for a Range

Given a sorted array of integers, find the starting and ending 
position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start, end, res = 0, len(A)-1, [-1, -1]
        while start < end:
            mid = (start+end)/2 
            if A[mid] < target: start = mid+1
            else: end = mid
        low = start if A[start]==target else -1
        if low == -1: return res
        start, end = low, len(A)
        while start < end:
            mid = (start+end)/2 
            if A[mid] > target: end = mid
            else: start = mid + 1
        high = start - 1
        res = [low, high]
        return res

if __name__=="__main__":
    A = [5, 7, 7, 8, 8, 10]
    target = 8
    print Solution().searchRange(A,target)

"""
Binary search.
First from the left part find the low bound.
Second from the right part find the high bound.
"""


