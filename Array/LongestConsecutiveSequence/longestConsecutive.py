#!/usr/bin/python

"""
Longest Consecutive Sequence 

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dic = {x:False for x in num}
        maxlen = -1
        for i in dic:
            if dic[i] == False:
                curr, len1 = i+1, 0
                while curr in dic and dic[curr] == False:
                    len1, dic[curr], curr = len1+1, True, curr+1
                curr, len2 = i-1, 0
                while curr in dic and dic[curr] == False:
                    len2, dic[curr], curr = len2+1, True, curr-1
                maxlen = max(maxlen, 1+len1+len2)
        return maxlen

if __name__=='__main__':
    A = [100, 4, 200, 1, 3, 2]
    print Solution().longestConsecutive(A)
   
"""
Note that it is not the classic DP problem, while this problem tests the data structure other than algorithm.

Since it requires O(n) solution, normal sort won't be work here. Hash probably is the best choice.
3 Steps:
1. create the hashmap to hold <num, index>
2. scan the num vector from left to right, for each num
               i, check whether num -1 is in the map  (loop)
              ii, check whether num+1 is in the map  (loop)
3. track the sequence length during scanning. 
"""

