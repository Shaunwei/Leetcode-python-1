#!/usr/bin/python

"""
Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown 
to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        res,st,end = num[0],0,len(num)-1
        while st <= end:
            mid = (st+end)/2 
            # skip the duplicates
            while num[mid]==num[end] and mid!=end:
                end -= 1
            while num[st]==num[mid] and st!=mid:
                st += 1
            # right part ordered
            if num[mid] < num[end] or mid == end: 
                res = min(res,num[mid])
                end = mid - 1
            else: # right part unordered
                res = min(res,num[st])
                st = mid + 1
        return res

if __name__=="__main__":
    arr = [4,5,6,6,7,7,0,1,2,2]
    print Solution().findMin(arr)

"""
Using binary search.
Same as the "Find Minimum in Rotated Sorted Array",
only minute different is to need skip duplicates. 
"""