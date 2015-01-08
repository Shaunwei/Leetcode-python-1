#!/usr/bin/python
"""
Merge Two Sorted Lists 

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import LListUtil
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dumhead = ListNode(0)
        curr = dumhead
        while True:
            if not l1:
                curr.next = l2
                break
            if not l2:
                curr.next = l1
                break
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dumhead.next

if __name__=="__main__":
    arr1 = LListUtil.randomArr(10,5)
    arr2 = LListUtil.randomArr(10,5)
    arr1.sort(); arr2.sort()
    l1 = LListUtil.buildList(arr1)
    l2 = LListUtil.buildList(arr2)
    LListUtil.printList(l1)
    LListUtil.printList(l2)
    sol = Solution()
    LListUtil.printList(sol.mergeTwoLists(l1,l2))     
