#!/usr/bin/python

"""
Search in Rotated Sorted Array II 

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            mid = (left+right) / 2
            if A[mid] == target: return True
            # the right side is rotated
            if A[mid] > A[left]:
                # A[left] may equal to target
                if A[left] <= target < A[mid]: right = mid - 1
                else: left = mid + 1
            elif A[mid] == A[left]:
                left += 1
            else: # A[mid]<A[left] the left side rotated 
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False       

if __name__=="__main__":
    A = [1,3,1,1,1]
    target = 3
    print Solution().search(A,target)

"""
When there's no duplicate, A[left] <= A[mid] means the right part 
is rotated. When there are duplicates, A[left] <= A[mid] is not certain.
E.g. A=[1,3,1,1,1], left = 0, right = 4, mid = 2, although A[left] <= A[mid], 
the left part is rotated. Here A[left] < A[mid] means the right part is rotated, 
when A[left] == A[mid] just left++.
"""

