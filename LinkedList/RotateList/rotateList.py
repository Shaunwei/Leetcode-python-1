#!/usr/bin/python

# Rotate List 

# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k==0: return head
        curr, listLen = head, 1
        while curr.next: curr, listLen = curr.next, listLen+1
        k = listLen - k % listLen
        if k == listLen:
            return head
        curr2, index = head, 1
        while index < k:
            curr2, index = curr2.next, index+1
        curr.next = head
        head = curr2.next
        curr2.next = None    
        return head

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
    #arr = list(range(1,10))
    arr = [1]
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.rotateRight(head,1))
