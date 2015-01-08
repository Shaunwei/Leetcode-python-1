#!/usr/bin/python
"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example:
Given 1->2->3->4, you should return the list as 2->1->4->3. 
Your algorithm should use only constant space. You may not modify the 
values in the list, only nodes itself can be changed.
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
    # @param a ListNode
    # @return a ListNode

    # the easy way, just swaps the values
    def swapPairs(self, head):
        if not head: return None
        curr = ListNode(0)
        curr.next = head
        head = curr
        while True:
            if not curr.next: break
            if not curr.next.next: break
            temp = curr.next.val
            curr.next.val = curr.next.next.val
            curr.next.next.val = temp
            curr = curr.next.next
        return head.next            

if __name__=="__main__":
    arr = list(range(1,10))
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().swapPairs(head))
    
'''
swap two nodes in linked list scheme::
nide1->node2->node3->nide4
first swap node1.next with node2.next 
node1.next = node2.next
node2.next = node2
second swap node2.next with node3.next
node2.next = node4
node3.next = node2
'''
