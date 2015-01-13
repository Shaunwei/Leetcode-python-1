#!/usr/bin/python
"""
Sort a linked list using insertion sort.
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
    def insertionSortList(self, head):
        if head is None: return None
        pivot = ListNode(0)
        pivot.next = head
        head = pivot
        while pivot.next:
            curr = head
            flag = False
            while curr != pivot:
                if curr.next.val > pivot.next.val:
                    temp = pivot.next
                    pivot.next = pivot.next.next
                    temp.next = curr.next
                    curr.next = temp
                    flag = True
                    break
                else:
                    curr = curr.next
            if not flag:
                pivot = pivot.next 
	return head.next        

if __name__=="__main__":
    arr = LListUtil.randomArr(20,10)
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.insertionSortList(head))     
