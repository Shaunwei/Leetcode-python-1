#!/usr/bin/python

# Remove Nth Node From End of List

# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Try to do this in one pass. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head: return head
        dumhead = ListNode(0)
        dumhead.next = head
        head = prev = dumhead
        count = 0
        while head.next:
            head = head.next
            count += 1
            if count > n:
                prev = prev.next
        prev.next = prev.next.next
        return dumhead.next
       
    def printList(self,head):
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
    arr = [1,2,3,4,5,6,7,8,9]
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.removeNthFromEnd(head,9))     
