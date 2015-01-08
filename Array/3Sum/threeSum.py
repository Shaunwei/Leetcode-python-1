#!/usr/bin/python

"""
3Sum

Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        for idx1 in xrange(len(num)):
            num1 = num[idx1]
            #skip the same element
            if idx1 >= 1 and num1 == num[idx1-1]: continue 
            idx2, idx3 = idx1+1, len(num)-1
            while idx2 < idx3:
                num2, num3 = num[idx2], num[idx3]
                if num1+num2+num3 == 0:
                    result.append([num1,num2,num3])
                    while idx2 < idx3: #skip the same element
                        idx2, idx3 = idx2+1, idx3-1
                        if num[idx2]!=num2 or num[idx3]!=num3: break
    	        elif num1+num2+num3 > 0:
                    while idx2 < idx3: #skip the same element
                        idx3 -= 1
                        if num[idx3]!=num3: break
                else:
                    while idx2 < idx3: #skip the same element
                        idx2 += 1
                        if num[idx2]!=num2: break
        return result

if __name__=="__main__":
    num = [-1, 0, 1, 2, -1, -4] 
    print Solution().threeSum(num)

"""
Two iterations:
1. sort the array first
2. 1st pointer from 1 to index end-2
3. while (2nd<3rd)

Conditions:
1. if (array[1st]+array[2nd]+array[3rd]==0), get one result, 2nd+1 and 3rd-1
2. if (array[1st]+array[2nd]+array[3rd]>0), 3rd-1
3. if (array[1st]+array[2nd]+array[3rd]<0), 2nd+1

Notice for the same elements, need to skip them.
"""


