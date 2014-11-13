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
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        q1, q2, lvl, res = [], [], [], []
        if root == None: return res
        q1.append(root)
        while True:
            while q1:
                node = q1.pop(0)
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
                lvl.append(node.val)    
            res.append(lvl)
            lvl, q1, q2 = [], q2, []
            if not q1:
                return res[::-1]

if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [3,9,20,'#','#',15,7]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    print Solution().levelOrderBottom(root)

"""
The output is slightly different from the classical level-order problem, 
which do not require the level information. So in this problem one way to 
get the level is using another queue to save the current level nodes.

The main steps are:
1. Push the root node into queue 1, which is level 1 (or 0)
2. Pop all the nodes from queue 1 to get the current level, for each poped node, 
push their left child and right child into queue 2.
3. Set queue 1 = queue 2.
4. clear queue 2.
"""