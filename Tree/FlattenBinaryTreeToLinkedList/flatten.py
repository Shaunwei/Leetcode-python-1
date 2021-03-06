#!/usr/bin/python

"""
Flatten Binary Tree to Linked List 

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree, 
each node's right child points to the next node of a pre-order traversal.
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
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        if not root.left: return
        else:
            p = root.left
            while p.right: p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None
        return
    

if __name__=="__main__":
    arr = [1,2,5,3,4,'#',6]
    sol = Solution()
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    sol.flatten(root)
    TreeUtil.print_tree_graph(root)

"""
Flatten left child first and then flatten right, after that attach left to roo.right.
"""