#!/usr/bin/python

"""
Symmetric Tree 

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' 
signifies a path terminator where no node exists below.

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
    def isSymmetric(self, root):
        if root == None: return True
        return self.checkSym(root.left, root.right)

    def checkSym(self, left, right):
        if left == right == None: return True
        if not(left and right): return False
        if left.val != right.val: return False
        return self.checkSym(left.left,right.right) \
            and self.checkSym(left.right,right.left)

if __name__=="__main__":
    # arr = [1,2,2,3,4,4,3]
    arr = [1,2,2,'#',3,'#',3]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    print sol.isSymmetric(root) 

"""
Recursive way, symmetric if:
1. root of left tree and right tree is all none or val equals
2. left.left equals right.right
3. left.right equals right.left
"""