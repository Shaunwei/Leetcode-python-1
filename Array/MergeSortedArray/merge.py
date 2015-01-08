#!/usr/bin/python

"""
Merge Sorted Array 

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) 
to hold additional elements from B. The number of elements initialized in A and B 
are m and n respectively.
"""

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        m, n, k = m-1, n-1, m+n-1
        while m>=0 and n>=0:
            if A[m] < B[n]: A[k], n = B[n], n-1
            else: A[k], m = A[m], m-1
            k -= 1
        while n>=0: A[k], k, n = B[n], k-1, n-1
    	
if __name__=="__main__":
    A = [2, 7, 11, 15,0,0,0]
    B = [3, 6 , 10]
    Solution().merge(A,4,B,3)
    print A

"""
Part of the merge sort, merge the arrays from the back by comparing the elements.
"""


