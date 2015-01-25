#!/usr/bin/python
"""
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity. 
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import LListUtil
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

if __name__=="__main__":
    l1 = sorted(LListUtil.randomArr(100,5))
    l2 = sorted(LListUtil.randomArr(100,5))
    l3 = sorted(LListUtil.randomArr(100,5))
    l4 = sorted(LListUtil.randomArr(100,5))
    l5 = sorted(LListUtil.randomArr(100,5))
    lists = [LListUtil.buildList(l1),LListUtil.buildList(l2),LListUtil.buildList(l3),LListUtil.buildList(l4),LListUtil.buildList(l5)]
    LListUtil.printLists(lists)
    LListUtil.printList(Solution().mergeKLists(lists))    

"""
heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.

heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant.

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. 
Runs more efficiently than heappush() followed by a separate call to heappop().
"""
