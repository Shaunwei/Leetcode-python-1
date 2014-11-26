#!/usr/bin/python

"""
First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in xrange(len(A)):
            while A[i] != i+1:
                if A[i]<=0 or A[i]>len(A) or A[i]==A[A[i]-1]:
                    break
                # swap A[i], A[A[i]-1]
                tmp=A[A[i]-1]; A[A[i]-1]=A[i]; A[i]=tmp
        for i in xrange(len(A)):
            if A[i] != i+1: return i+1
        return len(A) + 1

if __name__=="__main__":
    A = [3,4,-1,1]
    target = 2
    print Solution().firstMissingPositive(A)

"""
It is bucket, but cannot use extra space. So when A[i] != i, need to 
swap A[i] with A[A[i]], until A[i] == A[A[i]]. Then go through the array and 
find the miss match index and value.
Just notice, because need to a positive number, so we need start from i+1, 
since 0 is not positive integer, like A[i] = i+1.
"""