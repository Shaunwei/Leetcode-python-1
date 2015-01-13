#!/usr/bin/python

"""
Gas Station 

There are N gas stations along a circular route, where the amount 
of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of 
gas to travel from station i to its next station (i+1). You begin 
the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around 
the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        summ, total, k = 0, 0, -1
        for i in xrange(len(gas)):
            summ += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if summ < 0: summ, k = 0, i
        return k+1 if total >=0 else -1

if __name__=="__main__":
    gas = [3, 1, 2, 5, 4 ] 
    cost = [4, 1, 1, 2, 3]
    print Solution().canCompleteCircuit(gas,cost)

"""
If sum(gas) < sum(cost) then answer is -1, otherwise it should have answer is 
start index. 
Idea is if have start index, sum = gas[i] - cost[i], when sum < 0, ignore it, 
since total must >=0 then rest of sum should be >=0 
"""