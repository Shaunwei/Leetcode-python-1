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
        return self.mergeSort(head)
     
    def mergeSort(self, head):
        # base case
        if head is None or head.next is None: 
            return head 

        mid = self.makeHalf(head)
        first = self.mergeSort(head)
        mid = self.mergeSort(mid)
        return self.merge(first,mid)
    
    # merge sorted halves into one
    def merge(self, listA, listB):
        temphead = ListNode(0)
        curr = temphead
        while True:
            if not listA:
                curr.next = listB
                break
            if not listB:
                curr.next = listA
                break
            if listA.val < listB.val:
                curr.next = listA
                listA = listA.next
            else:
                curr.next = listB
                listB = listB.next
            curr = curr.next
       
        return temphead.next

    def makeHalf(self, head):
        slow = None
        fast = None
        if head is None or head.next is None:
            mid = None
     	else:
            slow = head
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                if fast is None:
                    break
                slow = slow.next

            mid = slow.next
            slow.next = None
        return mid

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
    sol.printList(sol.sortList(head))     
