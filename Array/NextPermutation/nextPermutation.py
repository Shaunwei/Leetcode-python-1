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
        numLen = len(num)
        #step 1
        partIndex = -1
        for i in reversed(xrange(numLen-1)):
            if num[i] < num[i+1]: 
                partIndex = i; 
                break
        #step 2
        if partIndex != -1:
            for i in reversed(xrange(numLen)):
                if num[i] > num[partIndex]:
                    #step 3
                    num[i],num[partIndex] = num[partIndex],num[i]
                    break
        #step 4
        i = partIndex + 1
        j = numLen - 1
        while i < j:
            num[i],num[j] = num[j],num[i]
            i, j = i+1, j-1
        return num

if __name__=="__main__":
    s = [1,2,3] 
    print Solution().nextPermutation(s)

"""
1. From right to left, find the first digit (PartitionNumber) which 
violates the increase trend.
2. From right to left, find the first digit which is larger than 
PartitionNumber, call it ChangeNumber.
3. Swap PartitionNumber and ChangeNumber.
4. Reverse all the digit on the right of partition index.
"""