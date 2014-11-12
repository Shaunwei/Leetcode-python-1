#!/usr/bin/python

"""
Insert Interval 

Given a set of non-overlapping intervals, insert a new interval 
into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according 
to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as 
[1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
import sys
sys.path.append("C:/code_temp/Leetcode-python/Tree")
import TreeUtil

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        res = []
        res.append(intervals[0])
        for i in xrange(1,len(intervals)):
            curr, prev = intervals[i], res[-1]
            if curr.start <= prev.end:
                prev.end = max(prev.end, curr.end)
            else:
                res.append(curr)
        return res

if __name__=="__main__":
    # invals = [[1,3],[6,9]]; newIn = [2,5]
    invals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newIn = [4,9]
    intervals = []
    for val in invals: intervals.append(Interval(val[0],val[1]))
    for val in Solution().insert(intervals,Interval(newIn[0],newIn[1])):
        print [val.start,val.end],

"""
This problem is similar as merge intervals.
1. Insert the new interval according to the start value.
2. Scan the whole intervals, merge two intervals if necessary.
"""