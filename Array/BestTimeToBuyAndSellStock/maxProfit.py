#!/usr/bin/python

"""
Best Time to Buy and Sell Stock 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices: return 0
        maxp, minp = 0, prices[0]
        for currp in prices:
            minp = min(minp,currp)
            maxp = max(maxp,currp-minp)
        return maxp

if __name__=='__main__':
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print Solution().maxProfit(A)
   
"""
Scan the array from left to right, update the max-profit by comparing max-profit so far with current price subtracts prioves lowest price.
"""

