#!/usr/bin/python

# Merge Two Sorted Lists 

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dumhead = ListNode(0)
        curr = dumhead
        while True:
            if not l1:
                curr.next = l2
                break
            if not l2:
                curr.next = l1
                break
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
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
    import random
    arr1 = random.sample(range(5),5)
    arr2 = random.sample(range(5),5)
    sol = Solution()
    l1 = buildList(arr1)
    l2 = buildList(arr2)
    sol.printList(l1)
    sol.printList(l2)
    sol.printList(sol.mergeTwoLists(l1,l2))     
