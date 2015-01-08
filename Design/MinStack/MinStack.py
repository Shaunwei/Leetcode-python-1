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
        self.st, self.minst = [], []

    def push(self, x):
        if not self.st or x <= self.getMin():
            self.minst.append(x)
        self.st.append(x)

    # @return nothing
    def pop(self):
        if self.st and self.minst:
            if self.st[-1] == self.getMin():
                self.minst.pop()
            self.st.pop()

    # @return an integer
    def top(self):
        if not self.st: return -1
        return self.st[-1]

    # @return an integer
    def getMin(self):
        if not self.minst: return 10**10
        return self.minst[-1] 

if __name__=="__main__":
    s = MinStack(); s.push(-1)#s.push(2); s.push(3); s.push(1); s.push(4);
    print s.top(), s.getMin(), #s.pop(), s.top()

"""
O(n) runtime, O(n) space - Extra stack:
If a new element is larger than the current minimum, we do not need to push 
it on to the min stack. When we perform the pop operation, check if the popped 
element is the same as the current minimum. If it is, pop it off the min stack too.
"""


