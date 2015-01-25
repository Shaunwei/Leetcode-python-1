#!/usr/bin/python

"""
Merge Intervals 

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals: return []
        intervals.sort(key=lambda x:x.start)
        res = []
        res.append(intervals[0])
        for i in xrange(1,len(intervals)):
            curr, prev = intervals[i], res[-1]
            if curr.start <= prev.end:
                res[-1].end = max(prev.end, curr.end) #merge
            else:
                res.append(curr)
        return res

if __name__=="__main__":
    # invals = [[1,3],[2,6],[8,10],[15,18]]
    invals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    intervals = []
    for val in invals: intervals.append(Interval(val[0],val[1]))
    for val in Solution().merge(intervals):
        print [val.start,val.end],

"""
To check the intersections between interval [a,b] and [c,d],  
there are four cases (equal not shown in the figures):
    a____b
c____d
--------------
a____b
     c____d
--------------
a_______b
    c___d
--------------
   a___b
c_______d
--------------
So the idea is simple. 
First sort the list according to the start value. 
Second, scan every interval, if it can be merged to the previous one, 
then merge them, else push it into the result list.
"""