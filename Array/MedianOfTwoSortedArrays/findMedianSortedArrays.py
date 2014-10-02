#!/usr/bin/python

# Median of Two Sorted Arrays 

# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        leng = len(A) + len(B)
        if leng%2 == 1:
            return self.getMedian(A,B,leng/2+1)
        else:
            return 0.5*(self.getMedian(A,B,leng/2)+self.getMedian(A,B,leng/2+1))

    def getMedian(self, A, B, k):
        # return kth smallest number of arrays A and B, 
        # assume len(A) <= len(B)
        Alen, Blen = len(A), len(B)
        if Alen > Blen:return self.getMedian(B,A,k)
        if Alen == 0:return B[k-1]
        if k == 1:return min(A[0],B[0])
        partA = min(k/2,Alen)
        partB = k - partA
        if A[partA-1] <= B[partB-1]:
            return self.getMedian(A[partA:],B,k-partA)
        else:
            return self.getMedian(A,B[partB:],k-partB)

if __name__=="__main__":
    arr1 = [1, 5, 7, 10, 13]
    arr2 = [4, 6, 8, 10, 12]
    print Solution().findMedianSortedArrays(arr1,arr2)
    
'''
First, as the two arrays are sorted. Median is the (m+n)/2+1 th element if m+n is odd, the average of (m+n)/2 th and (m+n)/2+1 th  if m+n is even. e.g.  [1,2,3],[5,6,7], the median is (3+5)/2 = 4.0. [1,2,3,4], [1,3,5,7,9], the median is 3.

As mentioned above, our task becomes find the Kth (K-1 and K) number in two arrays. Two pointers are used, one for array A and one for array B. The basic idea is count K elements from A and B according to the pointers. A better thought is that assign half of K to each side, cut the smaller array again and again, until (1) the smaller array is empty, output the (K-1)th (array starts from 0) element in the bigger array (2) K=1. Return min(A[0],B[0]);
'''
