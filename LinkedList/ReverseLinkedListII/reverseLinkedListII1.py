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
        for i in range(n-m):
            index1 = n - i
            index2 = m + i
            if index2 >= index1: return head
            first, second = head, head
            while index1-1>0: first,index1 = first.next,index1-1
            while index2-1>0: second,index2 = second.next,index2-1
            first.val, second.val = second.val, first.val
        return head

if __name__=="__main__":
    arr = list(range(1,10))
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.reverseBetween(head,1,8))

"""
This is easy way which reverses just value of nodes.
(1) the stop condition is the middle of the reversed sublist (m+n)/2
(2) for each element in the sublist, the swapping element is the next 
(n-m-(i-m)*2) element.
    e.g.
    1-2-3-4-5-6-7-8-9-10-null
      |             |
     m=2           n=9
    for 2, just get the next (n-m) element.

    1-9-3-4-5-6-7-8-2-10-null
        |         |
       i=3      idx=8
    next element 3, the swapping element is 8.
"""