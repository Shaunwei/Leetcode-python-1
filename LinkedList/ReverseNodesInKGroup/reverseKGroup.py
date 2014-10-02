#!/usr/bin/python

# Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5 

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
        curr = ListNode(0)
        curr.next = head
        head = pivot = curr
        while True:
            index = 0
            while pivot and index < k:
                pivot = pivot.next
                index += 1
            if not pivot: return head.next
            else:
                while curr.next != pivot:
                    second = curr.next
                    first = pivot.next
                    curr.next = curr.next.next
                    pivot.next = second
                    second.next = first
                for i in range(k): curr = curr.next 
                pivot = curr
        return head.next

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
    sol.printList(sol.reverseKGroup(head,4))
