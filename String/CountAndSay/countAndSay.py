#!/usr/bin/python

"""
Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in xrange(n-1):
            prev = news = ''
            num = 0
            for curr in s:
                if prev != '' and prev != curr:
                    news += str(num) + prev
                    num = 1
                else:
                    num += 1
                prev = curr
            news += str(num) + prev
            s = news
        return s

if __name__=="__main__":
    ns = [1,2,3,4,5,6]
    for n in ns:
        print Solution().countAndSay(n)
 
"""
The better problem declare:
when n=1 output string '1'(base case); when n=2, count the number of previous digit, since last string is '1', so output is '11; when n=3, previous string is '11', since there is two '1', so output is '21'; and when n=4, so there is one '2' and one '1', so output is '1211'.
"""


