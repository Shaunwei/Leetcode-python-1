#!/usr/bin/python

"""
Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level 
order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None: return []
        res, self.L = [], {}
        self.preOrder(root, 0)
        for i in sorted(self.L.keys(), reverse=True):
            res.append(self.L[i])
        return res
     
    def preOrder(self, root, level):
        if level in self.L:
            self.L[level].append(root.val)
        else:
            self.L[level] = [root.val]
        if root.left:
            self.preOrder(root.left, level + 1)
        if root.right:
            self.preOrder(root.right, level + 1)
        return
        


if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [3,9,20,'#','#',15,7]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    print Solution().levelOrderBottom(root)

"""
Use pre-order traversal first, and store the level number,
then output result.
"""