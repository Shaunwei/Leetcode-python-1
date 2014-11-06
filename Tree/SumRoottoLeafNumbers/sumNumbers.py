#!/usr/bin/python

"""
Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf 
path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
import sys
sys.path.append("C:/code_temp/Leetcode-python/Tree")
import TreeUtil

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None: return 0
        if root.left == None and root.right == None: return root.val
        self.res = 0
        if root.left: self.dfs(root.left, root.val)
        if root.right: self.dfs(root.right, root.val)
        return self.res
     
    def dfs(self, node, value):
        if node == None: return
        if node.left == None and node.right == None:
            self.res += 10 * value + node.val
        self.dfs(node.left, 10 * value + node.val)
        self.dfs(node.right, 10 * value + node.val)

if __name__=="__main__":
    arr = [1]#[1,2,3,4,5,6]
    root = TreeUtil.buildTree(arr)
    print Solution().sumNumbers(root) 

"""
Using dfs: 
Parent pass its value to its child, and child use that value multiple 
10 plus itself value as it own new value.
"""