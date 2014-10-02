#!/usr/bin/python

"""
Two Sum

Given an array of integers, find two numbers such that they add up to 
a specific target number.

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
        dic = {} # {val:[index]}
        for i in xrange(len(num)):
            dic[num[i]] = [i+1] if num[i] not in dic else dic[num[i]]+[i+1]
        for i in num:
            if target-i in dic:
                if i == target-i: 
                    if len(dic[i]) == 2: return (dic[i][0], dic[i][1])
                else:
                    if dic[i][0] < dic[target-i][0]: return (dic[i][0],dic[target-i][0])
                    else: return (dic[target-i][0], dic[i][0])
    	

if __name__=="__main__":
    num = [0,4,3,0] #[2, 7, 11, 15]
    target = 0 #9
    print Solution().twoSum(num, target)



