#!/usr/bin/python

"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.
"""
import sys
sys.path.append("C:/code_temp/py_temp/Leetcode/Tree")
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
    def minDepth(self, root):
        if root == None: return 0
        if root.left == None and root.right == None: return 1
        if root.right == None:
            return self.minDepth(root.left)+1
        if root.left == None:
            return self.minDepth(root.right)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1

if __name__=="__main__":
    arr1 = [5,4,8,11,13,4,7,2,1]
    sol = Solution()
    root1 = TreeUtil.buildTree(arr1)
    TreeUtil.print_tree_pre(root1);print
    print sol.minDepth(root1) 