#!/usr/bin/python
"""
Copy List with Random Pointer 

A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list. 
"""
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
        curr = head
        # copy a[i] value to new b[i], and 
        # let a[i]->random store in b[i].next,
        # let b[i] store in a[i]->random
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.random
            curr.random = newNode
            curr = curr.next
        curr = head
        # let b[i]->random point to b[i]->next->random
        while curr:
            newNode = curr.random
            newNode.random = newNode.next.random if newNode.next else None
            curr = curr.next
        newhead = head.random
        curr = head
        # restore a[i].random and b[i].next
        while curr:
            newNode = curr.random
            curr.random = newNode.next
            newNode.next = curr.next.random if curr.next else None 
            curr = curr.next  
        return newhead

def buildList(arr):
    head = RandomListNode(0)
    curr = head
    for i in arr:
        curr.next = RandomListNode(i)
        curr = curr.next

    return head.next

if __name__=="__main__":
    arr = list(range(1,10))
    head = buildList(arr)
    Solution().copyRandomList(head)
