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
   
    # Using heap, no Time Limit Exceeded
    def mergeKLists(self, lists):
        import heapq
        if len(lists) == 0: return None
        heap = []
        for node in lists:
            if node: heap.append((node.val,node))
        heapq.heapify(heap)
        curr = head = ListNode(0)
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
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

'''
heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.

heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant.

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. Runs more efficiently than heappush() followed by a separate call to heappop().
'''
