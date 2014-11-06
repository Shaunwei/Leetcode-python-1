#!/usr/bin/python

"""
Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along 
the longest path from the root node down to the 
farthest leaf node.
"""
import sys
sys.path.append("C:/code_temp/Leetcode-python/Tree")
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
    def maxDepth(self, root):
        if root == None: return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

if __name__=="__main__":
    arr1 = [5,4,8,11,13,4,7,2,1]
    sol = Solution()
    root1 = TreeUtil.buildTree(arr1)
    TreeUtil.print_tree_pre(root1);print
    print sol.maxDepth(root1) 