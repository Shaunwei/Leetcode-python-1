#!/usr/bin/python

"""
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.
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

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.buildBST(num,0,len(num)-1)

    def buildBST(self, num, start, end):
        if start - end > 0: return None
        mid = (start+end)/2
        root = TreeNode(num[mid])
        root.left = self.buildBST(num,start,mid-1)
        root.right = self.buildBST(num,mid+1,end)
        return root

if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    sol = Solution()
    root = Solution().sortedArrayToBST(arr)
    TreeUtil.print_tree_graph(root)

"""
Recuesively get array mid-element as root to build a BST.
"""