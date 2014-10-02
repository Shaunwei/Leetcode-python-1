#!/usr/bin/python

"""
3Sum Closest                                                                                                                       

Given an array S of n integers, find three integers in S such 
that the sum is closest to a given number, target. Return the 
sum of the three integers. You may assume that each input would 
have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        error = float("infinity")
        if len(num)<3:
            return 0
        for i in range(0, len(num)-2):
            begin = i+1
            end = len(num)-1
            while begin<end:
                if abs(num[i]+num[begin]+num[end]-target) < error:
                    error = abs(num[i]+num[begin]+num[end]-target)
                    result = num[i]+num[begin]+num[end]
                if num[i]+num[begin]+num[end] > target:
                    end -= 1
                else:
                    begin += 1
        return result

if __name__=="__main__":
    num = [1,1,1,0] #[-1, 2, 1, -4] 
    target = -100 # 1
    print Solution().threeSumClosest(num,target)

"""
The code is slight different from the 3 sum problem, 
just change the if condition, the key point is to use 
the abs() function to get the distances between the 
target and the output value.
"""


