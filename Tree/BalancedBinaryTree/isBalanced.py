#!/usr/bin/python

"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined 
as a binary tree in which the depth of the two subtrees of 
every node never differ by more than 1.
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
    # @return a boolean
    def isBalanced(self, root):
        return self.checkBlance(root)[1]

    # return tree height and bool balanced result
    def checkBlance(self, root):
        if root == None: return (0, True)
        lh, lblan = self.checkBlance(root.left)
        rh, rblan = self.checkBlance(root.right)
        return (max(lh,rh)+1, lblan and rblan and abs(lh-rh)<=1)

if __name__=="__main__":
    arr1 = [5,4,8,11,13,4,7,2,1]
    sol = Solution()
    root1 = TreeUtil.buildTree(arr1)
    TreeUtil.print_tree_pre(root1);print
    print sol.isBalanced(root1) 