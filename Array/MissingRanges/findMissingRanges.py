#!/usr/bin/python

"""
Missing Ranges

Given a sorted integer array where the range of elements are [0, 99] inclusive, 
return its missing ranges.

For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]
"""

class Solution:
    # @param A, a list of integer digits
    # @param lower, a integer
    # @param upper, a integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        ranges, prev = [], lower-1
        for i in xrange(len(A)+1):
            curr = upper+1 if i==len(A) else A[i]
            if curr - prev > 1:
                if prev+1==curr-1: tmpstr = str(prev+1) 
                else: tmpstr = str(prev+1)+'->'+str(curr-1)
                ranges.append(tmpstr)
            prev = curr
        return ranges
    	
if __name__=="__main__":
    A = [0, 1, 3, 50, 75]
    lower = 0; upper = 99
    print Solution().findMissingRanges(A,lower,upper)



