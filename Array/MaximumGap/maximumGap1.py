#!/usr/bin/python

"""
Maximum Gap

Given an unsorted array, find the maximum difference between the successive 
elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit 
in the 32-bit signed integer range.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2: return 0
        num = self.radixsort(num)
        res = abs(num[1] - num[0])
        for i in xrange(2,len(num)):
            res = max(res, abs(num[i] - num[i-1]))
        return res

    def radixsort(self, num):
        max_n = max(num)
        nd = 1
        while max_n / nd > 0:
            num = self.countsort(num, nd)
            nd = nd * 10
        return num

    def countsort(self, num, nd):
        count = [0]*10
        n = len(num)
        for i in xrange(0,n):
            count[ (num[i]/nd) %10] += 1  
        for i in xrange(1,10):
            count[i] += count[i-1]
        output = [0]*n
        for i in xrange(n-1,-1,-1):
            output[count[ (num[i]/nd)%10 ] - 1 ] = num[i]
            count[ (num[i]/nd)%10 ] -= 1
        return output
     
    
        
if __name__=="__main__":
    num = [1, 0, 1, 2, 1, 4] 
    print Solution().maximumGap(num)

"""
For this specific problem, bucket sort is not a good option because it usually 
works well on uniform distributions. Otherwise, in each bucket, the insertion 
sort may cause heavy burden on time complexity. Counting sort, has time complexity O(n + k), 
where k is the range of the elements. But when k > n^2, it is worse than the common 
sorting algorithms. So we use the radix sort for solving this problem.

To sort array according to each digit, counting sort is used. Note that, we only need to 
have a array of size 10 to store the frequencies of elements. This is because we only consider 
and sort a single digit in each iteration of Radix sort. 

The general form of counting sort is:
(1) Count the frequencies of each elements.  (count[a[i]] ++, this also considers the duplicates)
(2) Get the index of each number in the output array. (count[i]+= count[i-1])
(3) Put numbers in order. (output[count[a[i]] = a[i], count[a[i]]-- to handle the duplicates)
"""


