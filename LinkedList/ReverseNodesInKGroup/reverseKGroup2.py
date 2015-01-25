#!/usr/bin/python
"""
Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 
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
    def reverseKGroup(self, head, k):
        if not head: return None
        dumhead = ListNode(0)
        dumhead.next = head
        curr, listLen = head, 0
        while curr: curr, listLen = curr.next, listLen+1
        curr, prev, index = head, dumhead, 1
        prehead, preheadnext = dumhead, head
        while curr:
            if listLen-index < listLen%k: break
            nextN = curr.next
            curr.next = prev
            if index%k == 0:
                prehead.next = curr
                preheadnext.next = nextN
                prehead = preheadnext
                prev = prehead
                preheadnext = nextN
            else:
                prev = curr
            curr, index = nextN, index+1   
        return dumhead.next

if __name__=="__main__":
    arr = range(1,10)
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().reverseKGroup(head,4))

"""
Simliar as problem 'Swap Nodes in Pairs'.
when index meet times of K (index%K==0), then reverse the list segement.
Notice, for the last few nodes (list_Length-index < list_Length%k) do nothing.
"""