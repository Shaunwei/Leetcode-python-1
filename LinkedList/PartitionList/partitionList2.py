#!/usr/bin/python

"""
Partition List 

Given a linked list and a value x, partition it such that all nodes 
less than x come before nodes greater than or equal to x. 

You should preserve the original relative order of the nodes in each 
of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5. 
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
    def partition(self, head, x):
        if not head: return head
        pivot = ListNode(0)
        pivot.next = head
        prev = None
        while pivot and pivot.val < x:
            prev = pivot
            pivot = pivot.next
        if pivot:
            curr = prev
            while pivot:
                if pivot.val < x:
                    temp = curr.next
                    prev.next = pivot.next
                    curr.next = pivot
                    curr = pivot
                    pivot.next = temp
                    pivot = prev
                prev = pivot
                pivot = pivot.next 
        return head

if __name__=="__main__":
    arr = [1,4,3,2,5,2]
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().partition(head,3))       

"""
Scan from left to right, if met a node(pivot node) value larger than X, 
then insert all small nodes found later into the left of pivot node.
"""