#!/usr/bin/python

"""
Recover Binary Search Tree 

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. 
Could you devise a constant space solution?
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
    def recoverTree(self, root):
        self.prev = self.first = self.second = None
        self.dfs(root)
        if self.first and self.second:
            self.first.val,self.second.val=self.second.val,self.first.val
        return root  

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        if self.prev and node.val < self.prev.val:
            if not self.first: self.first, self.second = self.prev, node
            else: self.second = node 
        self.prev = node
        self.dfs(node.right)

if __name__=="__main__":
    arr = [4,3,10,1,6,'#',14,'#','#',8,7,13]
    # arr = [8,3,10,1,6,'#',14,'#','#',4,7,13]
    root = TreeUtil.buildLeetTree(arr)
    TreeUtil.print_tree_graph(root)
    root1 = Solution().recoverTree(root)
    TreeUtil.print_tree_graph(root1)

"""
DFS, in-order tree traversal recursively.
What we need is actually two pointers, which point to 2 tree nodes where is incorrect. 
Therefore, we only need to store these two pointers, and, we also need another pointer 
to store the previous element, in order to ompare if the current element is valid or not.

The last step is to replace the wrong pair's value. And the in-order traversal is to search the 
whole BST and find the wrong pairs.

Note that: 
(1)the previous element is NOT the root node of the current element, 
but the previous element in the "in-order" order; 
(2) To store the wrong pair, the first found wrong element is stored in first pointer, 
while the next is stored in the second pointer.
"""