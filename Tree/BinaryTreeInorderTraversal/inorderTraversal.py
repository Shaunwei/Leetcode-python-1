#!/usr/bin/python

"""
Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
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
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []; stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val) # in-order print out 
                root = root.right
        return res


if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [1,'#',2,3]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    TreeUtil.print_tree(root,'in-order');print
    print Solution().inorderTraversal(root)

"""
Doing in the iteratively way:
Using stack to main the traversal. when root is not null, put it in stack and
go to the left child (root = root.left), till no more left child, then pull out
the stack which the previous value, the go to the right child ( root = root.right )
"""