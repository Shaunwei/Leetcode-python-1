#!/usr/bin/python

# Median of Two Sorted Arrays 

# There are two sorted arrays A and B of size n. Find the median of the two sorted arrays. The overall run time complexity should be O(log (2n)).
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B, leng):
        if leng == 0:return 0
        if leng == 1:return (A[0]+B[0])*0.5
        if leng == 2:return (max(A[0],B[0])+min(A[1],B[1]))*0.5
        mA = (A[leng/2]+A[leng/2-1])*0.5 if leng%2==0 else A[leng/2]
        mB = (B[leng/2]+B[leng/2-1])*0.5 if leng%2==0 else B[leng/2]
        # If medians are equal then return either m1 or m2
        if mA == mB:return mA
        # if m1 < m2 then median must exist in ar1[m1....] and ar2[....m2]
        if mA < mB:
            if leng%2 == 0:
                return self.findMedianSortedArrays(A[leng/2-1:],B,leng-leng/2+1)
            else:
                return self.findMedianSortedArrays(A[leng/2:],B,leng-leng/2)
        # if m1 > m2 then median must exist in ar1[....m1] and ar2[m2...]
        else:
            if leng%2 == 0:
                return self.findMedianSortedArrays(B[leng/2-1:],A,leng-leng/2+1)
            else:
                return self.findMedianSortedArrays(B[leng/2:],A,leng-leng/2)

if __name__=="__main__":
    arr1 = [1, 5, 7, 10, 13]
    arr2 = [4, 6, 8, 10, 12]
    print Solution().findMedianSortedArrays(arr1,arr2,5)
    
'''
Algorithm:
1) Calculate the medians m1 and m2 of the input arrays ar1[] 
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one 
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one    
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays 
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get 
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
'''
