#!/usr/bin/python

"""
Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical 
and the nodes have the same value.
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
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == q == None: return True
        if not (p and q) or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__=="__main__":
    arr1 = [5,4,8,11,13,4,7,2,1]
    arr2 = [5,4,8,11,13,4,7,2,2]
    sol = Solution()
    root1 = TreeUtil.buildTree(arr1)
    root2 = TreeUtil.buildTree(arr2)
    TreeUtil.print_tree_graph(root1)
    TreeUtil.print_tree_graph(root2)
    print sol.isSameTree(root1,root2) 