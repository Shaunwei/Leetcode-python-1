#!/usr/bin/python

"""
Convert Sorted List to Binary Search Tree 

Given a singly linked list where elements are sorted in ascending order,
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        num = []
        while head:
            num.append(head.val)
            head = head.next
        return self.buildBST(num,0,len(num)-1)

    def buildBST(self, num, start, end):
        if start - end > 0: return None
        mid = (start+end)/2
        root = TreeNode(num[mid])
        root.left = self.buildBST(num,start,mid-1)
        root.right = self.buildBST(num,mid+1,end)
        return root

def buildList(arr):
    head = ListNode(0)
    curr = head
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next
    return head.next

if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    head = buildList(arr)
    sol = Solution()
    root = Solution().sortedListToBST(head)
    # TreeUtil.print_tree_level(root);print
    TreeUtil.print_tree_graph(root)

"""
Convert linked list to array first.
Recuesively get array mid-element as root to build a BST.
"""