#!/usr/bin/python

"""
Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        ratelen, candy = len(ratings), [1]*len(ratings)
        for i in xrange(ratelen-1):
            if ratings[i+1]>ratings[i] and candy[i+1]<=candy[i]:
                candy[i+1] = candy[i] + 1
        for i in reversed(xrange(1,ratelen)):
            if ratings[i-1]>ratings[i] and candy[i-1]<=candy[i]:
                candy[i-1] = candy[i] + 1
        return sum(candy)
    	

if __name__=="__main__":
    ratings = [1, 2, 2]
    print Solution().candy(ratings)

"""
Scan the rating array from left to right and then from right to left. 
In every scan just consider the rising order, assign +1 candies to the 
rising position.
"""