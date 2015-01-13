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
        if not head: return head
        dumhead = ListNode(0)                         
        dumhead.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            
                pre = dumhead                        
                while pre.next.val < curr.next.val: 
                    pre = pre.next
                tmp = curr.next                    
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dumhead.next        

if __name__=="__main__":
    arr = LListUtil.randomArr(20,10)
    sol = Solution()
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(sol.insertionSortList(head))     
