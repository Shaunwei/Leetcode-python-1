#!/usr/bin/python

"""
Validate Binary Search Tree 

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

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
    def isValidBST(self, root):
        infint = 10 ** 10
        return self.check(-infint, root, infint)

    def check(self, Min, root, Max):
        if root == None: return True
        if not Min < root.val < Max: return False
        return self.check(Min, root.left, root.val) \
            and self.check(root.val, root.right, Max)

if __name__=="__main__":
    arr1 = [0] # [5,4,8,11,13,6,7,2,1] #[1,1]
    sol = Solution()
    root1 = TreeUtil.buildTreeInOrder(arr1)
    root2 = TreeUtil.buildTree(arr1)
    print sol.isValidBST(root1) 
    print sol.isValidBST(root2) 

"""
Using left bound and right to validate.
Think more about the node than tree.
"""