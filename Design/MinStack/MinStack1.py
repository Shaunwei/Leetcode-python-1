#!/usr/bin/python

"""
Min Stack

Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.diff, self.minv = [], 10**10L

    def push(self, x):
        self.diff.append(long(x)-self.minv)
        if x < self.minv: self.minv = x

    # @return nothing
    def pop(self):
        if self.diff:
            d = self.diff.pop()
            self.minv = self.minv if d>=0 else self.minv-d

    # @return an integer
    def top(self):
        if not self.diff: return -1
        d = self.diff[-1]
        return int(d+self.minv) if d>=0 else int(self.minv)

    # @return an integer
    def getMin(self):
        return int(self.minv)

if __name__=="__main__":
    s = MinStack(); s.push(-1)#s.push(2); s.push(3); s.push(1); s.push(4);
    print s.top(), s.getMin(), #s.pop(), s.top()

"""
O(n) runtime, O(n) space - No Extra stack: (oj will Memory Limit Exceeded)
Use only one min varible and stack stroe the difference values.
For push process:
difference = value - min
update min when value < min
For pop process:
need update the min to LastMin 
astMin = min (when difference > 0)
LastMin = min - difference (when difference < 0)
For top process:
if difference > 0, then top value = difference + min
if difference < 0, then top value = min
"""


