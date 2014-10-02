#!/usr/bin/python

# Partition List 

# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. 

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def partition(self, head, x):
        if not head: return head
        headLess = currLess = ListNode(0)
        headGreat = currGreat = ListNode(0)
        prev, curr = None, head
        while curr:
            prev, curr = curr, curr.next
            if prev.val < x:
                currLess.next = prev
                currLess = currLess.next
                currGreat.next = None
            else:
                currGreat.next = prev
                currGreat = currGreat.next
                currGreat.next = None
        currLess.next = headGreat.next 
        return headLess.next
       
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
    arr = [1,4,3,2,5,2]
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.partition(head,3))     
