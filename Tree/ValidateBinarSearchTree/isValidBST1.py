#!/usr/bin/python

"""
Validate Binary Search Tree 

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies 
a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
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
    # @return a boolean
    def isValidBST(self, root):
        return self.verifyBST(root,False,False,0,0)

    def verifyBST(self, root, left, right, lmax, rmin):
        if root == None: return True
        if left and root.val >= lmax: return False
        if right and root.val <= rmin: return False
        leftValid = self.verifyBST(root.left,True,right,root.val,rmin)
        rightValid = self.verifyBST(root.right,left,True,lmax,root.val)
        return leftValid and rightValid

if __name__=="__main__":
    arr1 = [1,1] # [0] # [5,4,8,11,13,6,7,2,1]
    sol = Solution()
    root1 = TreeUtil.buildTreeInOrder(arr1)
    root2 = TreeUtil.buildTree(arr1)
    print sol.isValidBST(root1) 
    print sol.isValidBST(root2) 

"""
For each subtree, give it max and min bound, if outside return fasle.
But for root node there is no bound.
For each level root, left subtree max bound should less than root,
right subtree min bound should greater than root.
Notice that for recursive call, should input parent node value.
"""