#!/usr/bin/python
"""
Remove Duplicates from Sorted List 

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        curr = head
        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if __name__=="__main__":
    arr = [1,1,2,3,3]
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList( Solution().deleteDuplicates(head))     
