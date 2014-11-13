#!/usr/bin/python

"""
Binary Tree Postorder Traversal 

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

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
    def postorderTraversal(self, root):
        res = []; stack = []; pre = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif pre == stack[-1].right:
                pre = stack.pop()
                res.append(pre.val) #post-order print out
            else:
                root = stack[-1].right
                pre = None
        return res


if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [1,'#',2,3]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    TreeUtil.print_tree(root,'post-order');print
    print Solution().postorderTraversal(root)

"""
Doing in the iteratively way:
Using stack to main the traversal. when root is not null, put it in stack and
go to the left child (root = root.left), till no more left child, then pull out
the stack which the previous value, the go to the right child ( root = root.right ).
We need a varible (previous) to store the status of left child or right child, 
if previous is right child then we can pop out the root.
"""