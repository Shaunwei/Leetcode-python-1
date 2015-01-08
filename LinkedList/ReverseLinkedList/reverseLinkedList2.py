#!/usr/bin/python
"""
Reverse a linked list.
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
    # @param head, a ListNod
    # @return a ListNode
    # alternative way, fixed prev and curr val, 
    # and move curr to the end
    def reverseLinkedList(self, head): 
        if not head: return None
        dumhead = ListNode(0)
        dumhead.next = head
        prev = dumhead
        curr = prev.next
        while curr.next:
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp
        return dumhead.next

if __name__=="__main__":
    arr = list(range(1,10))
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.reverseLinkedList(head))
