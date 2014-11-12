#!/usr/bin/python

"""
Construct Binary Tree from Inorder and Postorder Traversal 

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
import sys
sys.path.append("C:/code_temp/Leetcode-python/Tree")
import TreeUtil

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder: return None # inorder is empty
        root = TreeNode(postorder[-1])
        rootIdx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        root.right = self.buildTree(inorder[rootIdx+1:], postorder[rootIdx:-1])
        return root 

if __name__=="__main__":
    inorder = [4,2,5,1,3,6]
    postorder = [4,5,2,6,3,1]
    root = Solution().buildTree(inorder,postorder)
    TreeUtil.print_tree_graph(root)

"""
Recuesive method:
1. Find the last node in the postorder vector, which is the root of the current tree.
2. Find the position of root node in the inorder vector, which divide the inorder vector 
into 2 sub tree inorder vectors. Left part is the left sub-tree, right part is the right sub-tree.
3. Do 1 and 2 for the right and left sub-tree, respectively.
(Updated in 201309)
e.g. The tree is:
        1
   2        3
4   5         6
Inorder:     425136
Postorder:   452631

So, first we have 1 as the root node, and find 1's position in inorder, 425  1  36
Then we search: inorder 36        as the right child, and  inorder:   425  as the left child
                postorder (452)63                          postorder: 452
"""