#!/usr/bin/python

# Reorder List

# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next: return
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # now slow is the mid point and do reverse
        fast = slow.next
        while fast.next:
            temp = slow.next
            slow.next = fast.next
            fast.next = fast.next.next
            slow.next.next = temp 
        # insert reverse part
        fast = head
        while slow != fast and slow.next:
            temp = fast.next
            fast.next = slow.next
            slow.next = slow.next.next
            fast.next.next = temp
            fast = fast.next.next              
          
    def printList(self,head):
        if not head: print "None",
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
    sol.reorderList(head)
    sol.printList(head)

'''
So the algorithm implemented below can be summarized as:
Step 1  Find the middle pointer of the linked list (you can use the slow/fast pointers)
Step 2  Reverse the second part of the linked list (from middle->next to the end)
Step 3  Do the reordering. (inset every element in the second part in between the elements in the first part)
'''    
