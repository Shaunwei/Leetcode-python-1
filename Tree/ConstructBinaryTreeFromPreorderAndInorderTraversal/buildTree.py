#!/usr/bin/python

"""
Construct Binary Tree from Preorder and Inorder Traversal 

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import TreeUtil

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not inorder: return None
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootIdx+1],inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:],inorder[rootIdx+1:])
        return root

if __name__=="__main__":
    inorder = [4,2,5,1,3,6]
    pretorder = [1,2,4,5,3,6]
    root = Solution().buildTree(pretorder,inorder)
    TreeUtil.print_tree_graph(root)

"""
Recursive method:
This problem is similar as Construct Binary Tree From Inorder 
And Postorder Traversal.
"""