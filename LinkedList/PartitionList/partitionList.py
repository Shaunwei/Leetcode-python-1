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
        headLess = currLess = ListNode(0)
        headGreat = currGreat = ListNode(0)
        prev, curr = None, head
        while curr:
            prev, curr = curr, curr.next
            if prev.val < x:
                currLess.next = prev
                currLess = currLess.next
                currLess.next = None
            else:
                currGreat.next = prev
                currGreat = currGreat.next
                currGreat.next = None
        currLess.next = headGreat.next 
        return headLess.next

if __name__=="__main__":
    arr = [1,4,3,2,5,2]
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().partition(head,3))     

"""
Use two linked lists to separately record nodes < x and nodes >= x.
"""