#!/usr/bin/python
"""
Linked List Cycle 

 Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 
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
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False 

if __name__=="__main__":
    import random
    arr = list(range(10))
    sol = Solution()
    head = LListUtil.buildList(arr)
    print sol.hasCycle(head)     
