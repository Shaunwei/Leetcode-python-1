#!/usr/bin/python

# Reverse a linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNod
    # @return a ListNode
    def reverseLinkedList(self, head):
        if not head: return None
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
                
        return prev

    def printList(self,head):
        if not head: print "None"
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
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.reverseLinkedList(head))
