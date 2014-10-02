#!/usr/bin/python

"""
4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such 
that a + b + c + d = target? Find all unique quadruplets in the array which 
gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. 
(ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4: return []
        resultSet, result = set(), []
        num.sort()
        for i in xrange(len(num)):
            for j in xrange(i+1,len(num)):
                k, l = j+1, len(num)-1
                while k < l:
                    summ = num[i]+num[j]+num[k]+num[l]
                    if summ > target: l -= 1
                    elif summ < target: k += 1
                    else:
                        if (num[i],num[j],num[k],num[l]) not in resultSet:
                            resultSet.add((num[i],num[j],num[k],num[l]))
                            result.append([num[i],num[j],num[k],num[l]])
                        k, l = k+1, l-1
        return result

if __name__=="__main__":
    num, target = [1, 0, -1, 0, -2, 2], 0 
    print Solution().fourSum(num,target)

"""
This version like 3 sum closest but TLE.
"""


