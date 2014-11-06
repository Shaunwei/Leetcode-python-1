#!/usr/bin/python

"""
Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None: return False
        if root.val == sum and root.left == None and root.right == None: return True
        if root.left != None and self.hasPathSum(root.left, sum - root.val): return True
        if root.right != None and self.hasPathSum(root.right, sum - root.val): return True
        return False

if __name__=="__main__":
    arr = [5,4,8,11,13,4,7,2,1]
    sol = Solution()
    root = TreeUtil.buildTree(arr)
    summ = 22
    TreeUtil.print_tree_pre(root);print
    print sol.hasPathSum(root,summ) 