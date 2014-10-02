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
        if head is None: return None
        pivot = ListNode(0)
        pivot.next = head
        head = pivot
        while pivot.next:
            curr = head
            flag = False
            while curr != pivot:
                if curr.next.val > pivot.next.val:
                    temp = pivot.next
                    pivot.next = pivot.next.next
                    temp.next = curr.next
                    curr.next = temp
                    flag = True
                    break
                else:
                    curr = curr.next
            if not flag:
                pivot = pivot.next 
	return head.next        
                 
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
    #arr = [5,2,4,6,1,3]
    #arr = [2,1]
    sol = Solution()
    head = buildList(arr)
    sol.printList(head)
    sol.printList(sol.insertionSortList(head))     
