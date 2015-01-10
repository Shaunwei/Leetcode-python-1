#!/usr/bin/python

"""
Unique Binary Search Trees II 

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(1, n)
 
    # return a list containing all root nodes of BSTs 
    #  constructed from [start, end]
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for n in xrange(start,end+1):
            leftList = self.dfs(start,n-1)
            rightList = self.dfs(n+1,end)
            for i in leftList:
                for j in rightList:
                    root = TreeNode(n)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

if __name__=="__main__":
    n = 3
    roots = Solution().generateTrees(n)
    for root in roots:
        TreeUtil.print_tree_graph(root)

"""
The basic idea is still using the DFS scheme. 
It is a little hard to think the structure of the argument list in the function. 
It is clear that for each tree/subtree, we will set the root as the start position to 
the end position, and recursively construct the left subtree with the left part and 
the right subtree with the right part.

So first we can have
void dfs (int st, int ed){
    if (st>ed) { // generate a null node }
    else{
      for(int i=st;i<=ed;i++){  
        dfs(st,i-1); //generate left subtree 
        dfs(i+1,ed); // generate right subtree
      }
    }
}

All the possible solutions of the tree are from the combinations of all the possible 
solutions of its left subtree, and its right subtree.  That is Left-Child X Right-Child.
So use a list to store all the roots of nodes.
"""