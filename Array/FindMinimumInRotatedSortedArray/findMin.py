#!/usr/bin/python

"""
Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown 
to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        res,st,end = num[0],0,len(num)-1
        while st <= end:
            mid = (st+end)/2 
            # right part ordered
            if num[mid] < num[end]: 
                res = min(res,num[mid])
                end = mid - 1
            else: # right part unordered
                res = min(res,num[st])
                st = mid + 1
        return res

if __name__=="__main__":
    arr = [4, 5, 6, 7, -1, 1, 2]
    print Solution().findMin(arr)

"""
Using binary search.
Since there is only 1 rotation, which means that if right part is unordered, 
the left part of array must be ordered.
1. right part is ordered (A[mid] < A[ed])
2. right part is unordered (A[mid] > A[ed])
"""