#!/usr/bin/python

# Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode

    # Time Limit Exceeded
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        head = ListNode(0)
        head.next = lists[0]
        for l2 in lists[1:]:
            l1 = head
            while l2:
		if not l1.next:
                    l1.next = l2
                    break
                if l1.next.val < l2.val:
                    l1 = l1.next
                else:
                    temp = l1.next
                    l1.next = l2
                    l2 = l2.next
                    l1.next.next = temp
                    l1 = l1.next
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

def printLists(lists):
        for head in lists:
            while head:
                print head.val,
                head = head.next
            print

if __name__=="__main__":
    import random
    arr1 = sorted(random.sample(range(100),5))
    arr2 = sorted(random.sample(range(100),5))
    arr3 = sorted(random.sample(range(100),5))
    arr4 = sorted(random.sample(range(100),5))
    arr5 = sorted(random.sample(range(100),5))
    sol = Solution()
    lists = [buildList(arr1),buildList(arr2),buildList(arr3),buildList(arr4),buildList(arr5)]
    printLists(lists)
    sol.printList(sol.mergeKLists(lists))     
