#!/usr/bin/python
"""
Remove Duplicates from Sorted List II 

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
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
    def deleteDuplicatesII(self, head):
        if not head or not head.next: return head
        dumhead = ListNode(0)
        dumhead.next = head
        prev = dumhead
        while prev.next:
            curr = prev.next
            while curr.next and curr.val==curr.next.val:
                curr = curr.next
            if curr != prev.next:
                prev.next = curr.next
            else:
                prev = prev.next
        return dumhead.next

if __name__=="__main__":
    arr = [1,2,3,3,4,4,5] # [1,1,1,2,3]
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().deleteDuplicatesII(head))     
