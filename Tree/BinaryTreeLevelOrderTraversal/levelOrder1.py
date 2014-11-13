#!/usr/bin/python

"""
Binary Tree Level Order Traversal 

Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import TreeUtil

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res, q = [], []
        if root == None:
            return res
        q.append([root, 1])
        while q:
            node, dep = q.pop()
            if len(res) < dep:
                res.append([node.val])
            else:
                res[dep-1].append(node.val)
            if node.right:
                q.append([node.right, dep + 1])        
            if node.left:
                q.append([node.left, dep + 1])
        return res

if __name__=="__main__":
    # arr = [1,2,3,4,5,6]
    arr = [3,9,20,'#','#',15,7]
    sol = Solution()
    # root = TreeUtil.buildTree(arr)
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    TreeUtil.print_tree_level(root);print
    print Solution().levelOrder(root)

"""
The basic idea is still traversing the binary tree in level order (up-down). 
We can just use a vector to store the nodes and its level, set a pointer, 
each time move forward one and push its children into the vector. 
When all the nodes are visited, the vector become the up-down nodes in 
level order with level information. A simple loop can handle the output requirement.
The complexity is O(n), n is the number of nodes in the binary tree.
"""