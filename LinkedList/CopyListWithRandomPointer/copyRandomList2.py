#!/usr/bin/python

# Copy List with Random Pointer 

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list. 

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return None
        # change N1->N2->N3...to N1->newN1->N2->newN2...
        curr, num = head, 0
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            newNode.random = curr.random
            curr, num = newNode.next, num+1
        # let newNode.random point to correct node
        curr = head.next
        for i in range(num):
            if curr.random: curr.random = curr.random.next
            if curr and curr.next: curr = curr.next.next
        # restore original list and get new list
        p1, p2, newhead = head, head.next, head.next
        for i in range(num-1):
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1, p2 = p1.next, p2.next
        p1.next, p2.next = None, None   
        return newhead

    def printList(self,head):
        if not head: print "None"
        while head:
            print head.label,
            head = head.next
        print

def buildList(arr):
    head = RandomListNode(0)
    curr = head
    for i in arr:
        curr.next = RandomListNode(i)
        curr = curr.next

    return head.next

if __name__=="__main__":
    arr = list(range(1,10))
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.copyRandomList(head))
