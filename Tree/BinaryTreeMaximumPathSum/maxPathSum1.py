#!/usr/bin/python

"""
Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
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
    # @param root, a tree node
    # @return an integer
    deep = 0
    def maxPathSum(self, root):
        if root == None: return 0
        # Solution.maxSum is set to infinitesimal every time 
        #  when a new test case starts
        if self.deep == 0: 
            self.maxSum = -10 ** 10
        self.deep += 1
        vLeft = self.maxPathSum(root.left)
        vRight = self.maxPathSum(root.right)
        self.deep -= 1
        self.maxSum = max(root.val + vLeft + vRight, self.maxSum)
        if self.deep == 0:
            return self.maxSum
        return max(root.val + vLeft, root.val + vRight, 0)

if __name__=="__main__":
    arr = [1,2,3,4,5,6] #[2,-1]
    root = TreeUtil.buildTree(arr)
    print Solution().maxPathSum(root) 

"""
Using level deep idea, when deep equals zero then return result.
"""