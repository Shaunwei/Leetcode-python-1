#!/usr/bin/python

"""
Remove Duplicates from Sorted Array 

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        slow = 0
        for fast in xrange(len(A)):
            if A[fast] == A[slow]:
                continue
            else:
                slow += 1
                A[slow] = A[fast]
        return slow + 1

if __name__=="__main__":
    s = [-1,0,0,0,0,3,3] #[1,1,2] 
    print Solution().removeDuplicates(s)

"""
The test result will be a numbers of distinct elements,
and array will become the front length(return result) of 
elements is distinct. 
"""
