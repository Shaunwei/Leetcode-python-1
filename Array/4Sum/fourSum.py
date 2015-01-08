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
        numLen, result, dic = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in xrange(numLen):
            for q in xrange(p+1,numLen):
                if num[p]+num[q] not in dic:
                    dic[num[p]+num[q]] = [(p,q)]
                else:
                    dic[num[p]+num[q]].append((p,q))
        for i in xrange(numLen-2):
            for j in xrange(i+1,numLen-2):
                tmp = target - num[i] - num[j]
                if tmp in dic:
                    for k in dic[tmp]:
                        if k[0] > j:
                            result.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in result]

if __name__=="__main__":
    num, target = [1, 0, -1, 0, -2, 2], 0 # [-3,-2,-1,0,0,1,2,3], 0 
    print Solution().fourSum(num,target)

"""
First sort num, then build a dictionary d, d[num[p]+num[q]] = 
[(p,q) pairs which satisfy num[p] + num[q]], here all (p,q) pairs satisfy p < q. 
Then use a nested for-loop to search, num[i] is the min number in quadruplet 
and num[j] is the second min number. The time complexity of checking whether d 
has the key target - num[i] - num[j] is O(1). If this key exists, add one 
quadruplet to the result. Use set() to remove duplicates in ressult, otherwise 
for input [-3,-2,-1,0,0,1,2,3], 0 there will be two [-3, 0, 1, 2] and two [-2, -1, 0, 3].
"""


