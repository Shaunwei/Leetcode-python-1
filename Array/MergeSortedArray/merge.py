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
        i,j,k = m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1
    	

if __name__=="__main__":
    A = [2, 7, 11, 15,0,0,0]
    B = [3, 6 , 10]
    Solution().merge(A,4,B,3)
    print A



