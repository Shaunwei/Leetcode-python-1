#!/usr/bin/python

"""
Swap a linked list elements m and n. 

For example:
Given 1->2->3->4->5->NULL, m=2 and n=4
return 1->4->3->2->5->NULL
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
    def swapTwoLinkedList(self, head, m, n):
        if not head: return None
        m,n = min(m,n),max(m,n)
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
        temp = second.next
        second.next = first.next
        first.next = temp
        temp = second.next.next
        second.next.next = first.next.next
        first.next.next = temp
        return dumhead.next 

    # more easy way, just swap the value of two nodes
    def swapTwoLinkedList2(self, head, m, n):
        if not head: return None
        m,n = min(m,n),max(m,n)
        first = head
        second = head
        count = 0
        while count < n-1 and first:
            first = first.next
            count += 1
            if count > n-m:
                second = second.next
        if not first: return None
        temp = first.val
        first.val = second.val
        second.val = temp
        return head             

    def printList(self,head):
        if not head: print "None",
        while head:
            print head.val,
            head = head.next
        print

def buildList(arr):
    head = ListNode(0)
    curr = head
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next

    return head.next

if __name__=="__main__":
    arr = list(range(1,10))
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().swapTwoLinkedList(head,8,9))
    LListUtil.printList(Solution().swapTwoLinkedList2(head,1,9))

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
