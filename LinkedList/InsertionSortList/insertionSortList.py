#!/usr/bin/python

# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dumhead = ListNode(0)                         
        dumhead.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            
                pre = dumhead                        
                while pre.next.val < curr.next.val: 
                    pre = pre.next
                tmp = curr.next                    
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
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
    #arr = random.sample(range(20),20)
    #arr = [5,2,4,6,1,3]
    arr = [2,1]
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.insertionSortList(head))     
