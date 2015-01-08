#!/usr/bin/python
"""
Rotate List 

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k==0: return head
        curr, listLen = head, 1
        while curr.next: curr, listLen = curr.next, listLen+1
        k = listLen - k % listLen
        if k == listLen: return head
        curr.next, index = head, 0
        while index < k: curr, index = curr.next, index+1
        head = curr.next
        curr.next = None    
        return head

if __name__=="__main__":
    arr = list(xrange(1,6))
    head = LListUtil.buildList(arr)
    k = 2
    LListUtil.printList(head)
    LListUtil.printList(Solution().rotateRight(head,k))

"""
First, get the length of the list, then make last node.next point to head.
Second, iterate from head until length-k%length, then break the node. 
"""