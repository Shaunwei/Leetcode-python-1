#!/usr/bin/python

"""
Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations:add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""

class TwoSum:
    dic = {}
    def add(self, number):
        if number not in self.dic: self.dic[number] = 1
        else: self.dic[number] += 1

    def find(self, value):	
        for i in self.dic:
            val = value - i
            if val==i and self.dic[i]>1: return True
            if val!=i and val in self.dic: return True
        return False

if __name__=="__main__":
    sol = TwoSum()
    sol.add(1); sol.add(3); sol.add(5);
    print sol.find(4), sol.find(7)
