#!/usr/bin/python

# Reverse Linked List II 

# Reverse a linked list from position m to n. Do it in-place and one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m=2 and n=4
# return 1->4->3->2->5->NULL

# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head: return None
        m,n = min(m,n),max(m,n)
        dumhead = ListNode(0)
        dumhead.next = head
        first = dumhead
        second = dumhead
        count = 0
        while count < n-1 and first.next:
            first = first.next
            count += 1
            if count > n-m:
                second = second.next
        if not first.next: return None
        temp1 = first.next.next
        curr = second.next
        prev = None
        while curr != temp1:
            temp2 = curr.next
            curr.next = prev
            prev = curr
            curr = temp2
        second.next = prev
        if curr:
            while prev.next:
                prev = prev.next
            prev.next = curr
        return dumhead.next
  
    # this is easy way which reverses just value of nodes
    def reverseBetween2(self, head, m, n):
        for i in range(n-m):
            index1 = n - i
            index2 = m + i
            if index2 >= index1:
                return head
            first = head
            second = head
            while index1-1 > 0:
                first = first.next
                index1 -= 1
            while index2-1 > 0:
                second = second.next
                index2 -= 1
            first.val,second.val = second.val,first.val
	   
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
    arr = list(range(1,10))
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    #sol.printList(sol.reverseBetween2(head,2,9))
    sol.printList(sol.reverseBetween(head,2,1))
