#!/usr/bin/python

# Linked List Cycle 

#  Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        fast = head
        slow = head
        while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
              if slow == fast:
                  return True
        return False 

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
    head.next.next.next.next = head.next
    return head.next

if __name__=="__main__":
    import random
    #arr = random.sample(range(20),10)
    arr = list(range(10))
    sol = Solution()
    head = buildList(arr)
    #sol.printList(head)
    print sol.hasCycle(head)     
