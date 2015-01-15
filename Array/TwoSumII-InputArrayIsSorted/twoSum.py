#!/usr/bin/python

"""
Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 

Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if not num: return None
        i, j = 0, len(num)-1
        while i < j:
            x = num[i] + num[j]
            if x < target: i += 1
            elif x > target: j -= 1
            else: return (i+1,j+1)
        return None 
    	
if __name__=="__main__":
    num = [2, 7, 11, 15]
    target = 9
    print Solution().twoSum(num, target)

"""
Greedy algorithm. Two pointers, one from the beginning and one from the end.
Both move to the middle.
"""