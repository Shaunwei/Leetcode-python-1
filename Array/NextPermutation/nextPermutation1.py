#!/usr/bin/python

"""
Next Permutation  

Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible 
order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding 
outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        k, l = -1, 0
        #step 1
        for i in xrange(len(num)-1):
            if num[i] < num[i+1]: k = i
        if k == -1: num.reverse(); return num
        #step 2
        for i in xrange(len(num)):
            if num[i] > num[k]: l = i
        #step 3
        num[l],num[k] = num[k],num[l]
        #step 4
        return num[:k+1]+list(reversed(num[k+1:]))


if __name__=="__main__":
    s = [1]#[1,2,3] 
    print Solution().nextPermutation(s)

"""
Step 1: Find the largest index k, such that A[k]<A[k+1]. 
If not exist, this is the last permutation. (in this    
problem just sort the vector and return.)
Step 2: Find the largest index l, such that A[l]>A[k].
Step 3: Swap A[k] and A[l].
Step 4: Reverse A[k+1] to the end.
"""