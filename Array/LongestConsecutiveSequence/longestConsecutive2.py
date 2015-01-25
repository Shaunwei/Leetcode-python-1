#!/usr/bin/python

"""
Longest Consecutive Sequence 

Given an unsorted array of integers, find the length of the longest consecutive 
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        maxlen = 0
        for i in num:
            count, left, right = 1, i-1, i+1
            while left in num: num.remove(left);count,left = count+1, left-1
            while right in num: num.remove(right);count,right = count+1, right+1
            maxlen = max(maxlen,count)
        return maxlen

if __name__=='__main__':
    A = [100, 4, 200, 1, 3, 2]
    print Solution().longestConsecutive(A)
   
"""
Note that it is not the classic DP problem, while this problem tests the data structure 
other than algorithm.

Since it requires O(n) solution, normal sort won't be work here. Hash probably is the best choice.
3 Steps:
1. create the hashmap to hold <num, index>
2. scan the num vector from left to right, for each num
   i, check whether num-1 is in the map  (loop)
   ii, check whether num+1 is in the map  (loop)
3. track the sequence length during scanning. 

After an element is checked, it should be removed from the set. Otherwise, time complexity 
would be O(mn) in which m is the average length of all consecutive sequences.

This is version is TLE.
"""

