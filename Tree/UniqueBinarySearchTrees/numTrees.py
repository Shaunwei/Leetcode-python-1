#!/usr/bin/python

"""
Unique Binary Search Trees 

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import TreeUtil

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [0 for i in xrange(n+1)]
        dp[0] = 1
        for numNode in xrange(1, n+1):
            for numLeftNode in xrange(numNode):
                dp[numNode] += dp[numLeftNode] * dp[numNode-1-numLeftNode]
        return dp[n]


if __name__=="__main__":
    n = 3
    print Solution().numTrees(n)

"""
DP works well in this problem.

For each sequence from 1 to n, # of BSTs equals:
Sum of BSTs where each number (from 1 to n) is considered as the root node.
For each node, # of BSTs equals:
# of bsts of its left child times # of bsts of its right child.


Denote bst[i] = the number of BSTs can be constructed that store values from 1..n.

n = 1,  Node = {1},      bst[1]  = 1

n = 2,  Node = {1, 2}
when 1 is the root node, there is 1 bst
   1
    \
    2
when 2 is the root node, there is 1 bst
   2
  /
1
bst[2] = 2

n = 3,  Node = {1, 2, 3} 
when 1 is the root node, bst[3] =  bst[3] + bst[2] where stores 2 values (2 and 3)
     1                   1                   1
      \           =       \                   \
 BSTs of {2,3}             2                   3
                            \                 /
                             3               2
when 2 is the root node, bst[3] =  bst[3] + bst[1]
          2
         / \
        1   3
when 3 is the root node, bst[3] =  bst[3] + bst[2] where stores 2 values (1 and 2)
     3                     3                   3
    /             =       /                   /
 BSTs of {1,2}           2                   1
                        /                     \
                       1                       2

Formula: 
when node = 0 denote dp[0] = 1;
dp[n] += dp[k] * dp[n-1-k]
"""