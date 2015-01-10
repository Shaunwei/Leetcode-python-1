#!/usr/bin/python

"""
Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root: return []
        res = []
        self.buildPath(root,sum,[],res)
        return res
         
    def buildPath(self, root, sum, currPath, res):
        if not root: return
        currval = root.val
        currPath.append(currval)
        if not root.left and not root.right:
            if currval==sum: res.append(list(currPath))
        self.buildPath(root.left,sum-currval,currPath,res)
        self.buildPath(root.right,sum-currval,currPath,res)
        currPath.pop()

if __name__=="__main__":
    # arr = [5,4,8,11,13,4,7,2,1]
    arr = [5,4,8,11,'#',13,4,7,2,'#','#',5,1]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    summ = 22
    TreeUtil.print_tree_graph(root)
    print sol.pathSum(root,summ) 