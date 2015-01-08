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
    def reverseLinkedList(self, head):
        if not head: return None
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp        
        return prev

if __name__=="__main__":
    arr = list(range(1,10))
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.reverseLinkedList(head))
