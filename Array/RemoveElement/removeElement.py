#!/usr/bin/python

"""
Remove Element 

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        newlen = 0
        for i in A:
            if elem != i:
                A[newlen] = i
                newlen += 1
        return newlen

if __name__=="__main__":
    A = [4,2,3,4,5,6]
    elem = 4
    print Solution().removeElement(A, elem)
