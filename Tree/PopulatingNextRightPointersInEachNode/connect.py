#!/usr/bin/python

"""
Populating Next Right Pointers in Each Node 

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is 
no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at 
    the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
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
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None: return
        curNodeNum = 0
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop(0)
            curNodeNum += 1
            if curr.left:
                queue.append(curr.left)
                queue.append(curr.right)
            curr.next = None if curNodeNum & (curNodeNum + 1) == 0 else queue[0]

   

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7]
    sol = Solution()
    root = TreeUtil.buildTree(arr)
    TreeUtil.print_tree_graph(root)
    # Solution().connect(root)

"""
Use a queue to traverse the binary tree by level. When we meet the 
1st, 3rd, 7th, 15th, 31th... node (note that they are close to 2^n), 
assign None to their "next" field. Bit operation can be used to check 
whether N is 1, 3, 7, 15, 31... or not. N & (N + 1) == 0
"""