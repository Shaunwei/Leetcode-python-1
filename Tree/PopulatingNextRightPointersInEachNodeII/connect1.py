#!/usr/bin/python

"""
Populating Next Right Pointers in Each Node II 

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None: return
        que = []
        que.append([root, 1])
        while que:
            node, lvl = que.pop(0)
            if node.left: que.append([node.left,lvl+1])
            if node.right: que.append([node.right,lvl+1])
            if not que: return
            if lvl == que[0][1]: node.next = que[0][0]

if __name__=="__main__":
    arr = [1,2,3,4,5,'#',7]
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    Solution().connect(root)

"""
When traversing the current level, build the next level.
"""