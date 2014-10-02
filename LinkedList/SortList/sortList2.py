#!/usr/bin/python

# Sort List 

# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        length = 0
        curr = head;
        while curr != None:
            length += 1
            curr = curr.next
        return self.mergeSort(head, length)
     
    def mergeSort(self, head, length):
        # base case
        if length == 1 or length == 0: return head
         
        # sort the two halves of the list
        prev = curr = head
        for i in xrange(length / 2): curr = curr.next
        for i in xrange(length / 2 - 1): prev = prev.next
        prev.next = None
        head1 = self.mergeSort(head, length / 2)
        head2 = self.mergeSort(curr, length - length / 2)
         
        # merge sorted halves into one
        if head1.val <= head2.val:
            curr = newHead = ListNode(head1.val)
            head1 = head1.next
        else:
            curr = newHead = ListNode(head2.val)
            head2 = head2.next
        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = ListNode(head1.val)
                head1 = head1.next
            else:
                curr.next = ListNode(head2.val)
                head2 = head2.next
            curr = curr.next
        while head1:
            curr.next = ListNode(head1.val)
            head1 = head1.next
            curr = curr.next
        while head2:
            curr.next = ListNode(head2.val)
            head2 = head2.next
            curr = curr.next
        return newHead
    
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
    arr = random.sample(range(20),20)
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    
    sorthead = sol.sortList(head) 
    #sol.printList(sorthead)     
