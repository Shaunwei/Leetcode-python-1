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
import math
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if not num or len(num)<2: return 0
        maxi, mini = max(num), min(num)
        gap = int(math.ceil(float(maxi-mini)/(len(num)-1)))
        bucketNum = int(math.ceil(float(maxi-mini)/gap))
        bucketsMin = [10**10] * bucketNum
        bucketsMax = [-10**10] * bucketNum
        for i in xrange(len(num)):
            if num[i]==maxi or num[i]==mini: continue
            idx = (num[i]-mini)/gap
            bucketsMin[idx] = min(bucketsMin[idx], num[i])
            bucketsMax[idx] = max(bucketsMax[idx], num[i])
        ans = -10**10
        previous = mini
        for i in xrange(bucketNum):
            if bucketsMin[i]==10**10 or bucketsMax[i]==-10**10: continue
            ans = max(ans, bucketsMin[i]-previous)
            previous = bucketsMax[i];print ans
        ans = max(ans, maxi-previous)
        return ans

if __name__=="__main__":
    num = [19,20,11,13]#[1, 0, 1, 2, 1, 4] 
    print Solution().maximumGap(num)

"""
Suppose there are N elements and they range from A to B.

Then the maximum gap will be no smaller than ceiling[(B - A) / (N - 1)]

Let the length of a bucket to be len = ceiling[(B - A) / (N - 1)], then 
we will have at most num = (B - A) / len + 1 of bucket

for any number K in the array, we can easily find out which bucket it belongs 
by calculating loc = (K - A) / len and therefore maintain the maximum and minimum 
elements in each bucket.

Since the maximum difference between elements in the same buckets will be at most len - 1, 
so the final answer will not be taken from two elements in the same buckets.

For each non-empty buckets p, find the next non-empty buckets q, then q.min - p.max 
could be the potential answer to the question. Return the maximum of all those values.
"""


