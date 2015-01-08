#!/usr/bin/python
"""
Reverse Linked List II 

Reverse a linked list from position m to n. Do it in-place and one-pass.

For example:
Given 1->2->3->4->5->NULL, m=2 and n=4
return 1->4->3->2->5->NULL

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list
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
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head: return None
        dumhead = ListNode(0)
        dumhead.next = head
        first = dumhead
        second = dumhead
        count = 0
        while count < n-1 and first.next:
            first = first.next
            count += 1
            if count > n-m:
                second = second.next
        if not first.next: return None
        temp1 = first.next.next
        curr = second.next
        prev = None
        while curr != temp1:
            temp2 = curr.next
            curr.next = prev
            prev = curr
            curr = temp2
        second.next = prev
        if curr:
            while prev.next:
                prev = prev.next
            prev.next = curr
        return dumhead.next

if __name__=="__main__":
    arr = list(range(1,10))
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.reverseBetween(head,1,8))
