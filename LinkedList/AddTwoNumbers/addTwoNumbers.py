#!/usr/bin/python
"""
Add Two Numbers

You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain 
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dumhead = ListNode(0)
        carry = 0
        head = dumhead
        while carry or l1 or l2:
            node = ListNode(carry)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            carry = node.val / 10
            node.val %= 10
            head.next = node
            head = head.next
        return dumhead.next 

if __name__=="__main__":
    arr1 = LListUtil.randomArr(10,5)
    arr2 = LListUtil.randomArr(10,5)
    l1 = LListUtil.buildList(arr1)
    l2 = LListUtil.buildList(arr2)
    LListUtil.printList(l1)
    LListUtil.printList(l2)
    LListUtil.printList(Solution().addTwoNumbers(l1,l2))
