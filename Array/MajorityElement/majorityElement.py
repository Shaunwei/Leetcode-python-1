#!/usr/bin/python

"""
Majority Element

Given an array of size n, find the majority element. The majority element is the element 
that appears more than |_n/2_| times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        cand, count = 0, 0
        for i in num:
            if count==0: cand,count= i,1
            else:
                if i == cand: count += 1
                else: count -= 1
        return cand 

if __name__=="__main__":
    num = [1, 1, 2, 2, 2, 3] 
    print Solution().majorityElement(num)

"""
1. Runtime: O(n), Space: O(n) -- Hash table: Maintain a hash table of the counts of each element, 
then find the most common one.
2. Average runtime: O(n), Worst case runtime: Infinity -- Randomization: Randomly pick an element 
and check if it is the majority element. If it is not, do the random pick again until you find the 
majority element. As the probability to pick the majority element is greater than 1/2, the expected 
number of attempts is < 2.
3. Runtime: O(n log n) -- Divide and conquer: Divide the array into two halves, then find the majority 
element A in the first half and the majority element B in the second half. The global majority element 
must either be A or B. If A == B, then it automatically becomes the global majority element. If not, 
then both A and B are the candidates for the majority element, and it is suffice to check the count 
of occurrences for at most two candidates. The runtime complexity, T(n) = T(n/2) + 2n = O(n logn).
4. Runtime: O(n) -- Moore voting algorithm: We maintain a current candidate and a counter initialized 
to 0. As we iterate the array, we look at the current element x:
    If the counter is 0, we set the current candidate to x and the counter to 1.
    If the counter is not 0, we increment or decrement the counter based on whether x is the current candidate.
    After one pass, the current candidate is the majority element. Runtime complexity = O(n).
5. Runtime: O(n) -- Bit manipulation: We would need 32 iterations, each calculating the number of 1's for 
the ith bit of all n numbers. Since a majority must exist, therefore, either count of 1's > count of 0's 
or vice versa (but can never be equal). The majority number's ith bit must be the one bit that has the greater count.
"""