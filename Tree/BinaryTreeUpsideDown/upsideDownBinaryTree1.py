#!/usr/bin/python

"""
Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes 
with a sibling (a left node that shares the same parent node) or empty, 
flip it upside down and turn it into a tree where the original right 
nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
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
    # @return a tree node
    def upsideDownBinaryTree(self, root):
        p, parent, parentR = root, None, None
        while p:
            left = p.left
            p.left = parentR
            parentR = p.right
            p.right = parent
            parent = p
            p = left
        return parent

if __name__=="__main__":
    arr = [1,2,3,4,5]
    root = TreeUtil.buildTree(arr)
    TreeUtil.print_tree_graph(root)
    root1 = Solution().upsideDownBinaryTree(root)
    TreeUtil.print_tree_graph(root1)

"""
Where the original right nodes turned into left leaf nodes,
Let the original tree left node be a new node p, so we get:
p.left = parent.right
p.right = parent
"""