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
    def maxPathSum(self, root):
        self.maxSum = -10**10
        self.dfs(root)
        return self.maxSum
     
    def dfs(self, node):
        if node == None: return 0
        leftVal = self.dfs(node.left)
        rightval = self.dfs(node.right)
        self.maxSum = max(self.maxSum, leftVal+rightval+node.val)
        return max(leftVal+node.val,rightval+node.val,0)

if __name__=="__main__":
    arr = [1,2,3,4,5,6] #[2,-1]
    root = TreeUtil.buildTree(arr)
    print Solution().maxPathSum(root) 

"""
Using dfs:
The max path can be root + left-child or root + right-child or only root.
And because node value can be negative, so if curr-root or curr-root + left-child
or curr-root + right-child less than zero then ignore it and return zero. 
"""