#!/usr/bin/python
"""
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity. 
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
    # @param a list of ListNode
    # @return a ListNode

    # Time Limit Exceeded
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        head = ListNode(0)
        head.next = lists[0]
        for l2 in lists[1:]:
            l1 = head
            while l2:
                if not l1.next:
                    l1.next = l2
                    break
                if l1.next.val < l2.val:
                    l1 = l1.next
                else:
                    temp = l1.next
                    l1.next = l2
                    l2 = l2.next
                    l1.next.next = temp
                    l1 = l1.next
        return head.next

if __name__=="__main__":
    l1 = sorted(LListUtil.randomArr(100,5))
    l2 = sorted(LListUtil.randomArr(100,5))
    l3 = sorted(LListUtil.randomArr(100,5))
    l4 = sorted(LListUtil.randomArr(100,5))
    l5 = sorted(LListUtil.randomArr(100,5))
    lists = [LListUtil.buildList(l1),LListUtil.buildList(l2),LListUtil.buildList(l3),LListUtil.buildList(l4),LListUtil.buildList(l5)]
    LListUtil.printLists(lists)
    LListUtil.printList(Solution().mergeKLists(lists))    
