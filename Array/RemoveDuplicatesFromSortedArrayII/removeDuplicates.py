#!/usr/bin/python

"""
Remove Duplicates from Sorted Array II 

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        slow = 0
        count = 0
        for fast in xrange(1,len(A)):
            if A[fast] == A[fast-1]:
                count += 1
                if count <= 1:
                    slow += 1
                    A[slow] = A[fast]
            else:
                count = 0
                slow += 1
                A[slow] = A[fast]
        return slow + 1

if __name__=="__main__":
    s = [1,1,1,2,2,3]
    print Solution().removeDuplicates(s)

"""
The test result will be a numbers of distinct elements,
and array will become the front length(return result) of 
elements is distinct. 
"""
