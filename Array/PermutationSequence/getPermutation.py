#!/usr/bin/python

"""
Permutation Sequence 

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
import math
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        result = ''
        k -= 1 # count from 0
        factorial = math.factorial(n-1)
        num = [i for i in xrange(1, n + 1)]
        for i in reversed(xrange(n)):
            curr = num[k/factorial]
            result += str(curr)
            num.remove(curr)
            if i != 0:
                k %= factorial
                factorial /= i
        return result

if __name__=="__main__":
    n, k = 3, 5 # 9, 54494 #
    print Solution().getPermutation(n,k)

"""
Let num = [1,2,3,...,n]. kth-permutation = digit*(n-1)!, so the first digit is k/(n-1)!, 
then let k = k % (n-1)! and remove this digit from num. The second digit is k/(n-2)!, 
then let k = k % (n-2)! and remove this digit from num and so on.
"""