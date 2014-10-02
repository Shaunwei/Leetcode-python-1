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
        nlen = len(num)
        minVal = float('infinity')
        result = None
        for i in range(nlen):
            # skip the duplicate elements
            if i >= 1 and num[i] == num[i-1]: continue 
            start, end = i+1, nlen-1
            while start < end:
                summ = num[i] + num[start] + num[end]
                if summ == target:
                    minVal, result = 0, summ
                    break
                if summ < target:
                    if target - summ < minVal:
                        minVal, result = target-summ, summ
                    start += 1
                else:
                    if summ - target < minVal:
                        minVal, result = summ-target, summ
                    end -= 1
        return result

if __name__=="__main__":
    num = [1,1,1,0] #[-1, 2, 1, -4] 
    target = -100 # 1
    print Solution().threeSumClosest(num,target)
