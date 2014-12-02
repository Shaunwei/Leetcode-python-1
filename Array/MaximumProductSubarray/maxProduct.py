#!/usr/bin/python

"""
Maximum Product Subarray

Find the contiguous subarray within an array (containing at 
least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
      res = maxp = minp = A[0]
      for i in xrange(1,len(A)):
        maxtmp, mintmp = maxp, minp
        maxp = max(A[i]*maxtmp,A[i]*mintmp,A[i])
        minp = min(A[i]*maxtmp,A[i]*mintmp,A[i])
        res = max(res, maxp)
      return res

if __name__=="__main__":
    arr = [2,3,-2,4]
    print Solution().maxProduct(arr)


"""
An O(n) solution analysis:
Sscan the whole array, need to consider two cases:
(1) negative numbers:
Store the minimum product to handle the case that new element < 0.
Because if current element < 0, the product of two negative numbers 
(new element, and minimum product before the new element) become positive.
(2) zeros:
When meets zero, current max and min product become 0, new search is 
needed from the next element.

Dynamic programming formula:
f(k) = Largest product subarray, from index 0 up to k.
g(k) = Smallest product subarray, from index 0 up to k.
f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )
g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )
"""
