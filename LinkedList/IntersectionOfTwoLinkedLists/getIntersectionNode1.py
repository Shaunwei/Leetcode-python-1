#!/usr/bin/python

"""
Intersection of Two Linked Lists

Write a program to find the node at which the intersection 
of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 -> a2
                    \
                     c1 -> c2 -> c3
                    /            
B:     b1 -> b2 -> b3
begin to intersect at node c1.

Notes:
* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.
"""
from sys import path as path1; from os import path as path2
path1.append(path2.dirname(path2.dirname(path2.abspath(__file__))))
import LListUtil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        pA,pB,tailA,tailB = headA,headB,None,None 
        while True:
            if not pA: pA = headB
            if not pB: pB = headA
            if not pA.next: tailA = pA
            if not pB.next: tailB = pB
            #The two links have different tails. So just return null;
            if tailA and tailB and tailA!=tailB: return None
            if pA == pB: return pA
            pA, pB = pA.next, pB.next        

if __name__=="__main__":
    l1 = LListUtil.buildList([2,3])
    l2 = LListUtil.buildList([4,5,6])
    l3 = LListUtil.buildList([8,9,10])
    l1.next.next = l3; l2.next.next.next = l3
    LListUtil.printList(l1); LListUtil.printList(l2);
    print (Solution().getIntersectionNode(l1,l2)).val

"""
Two pointer solution (O(n+m) running time, O(1) memory): (Standard solution) 
Maintain two pointers pA and pB initialized at the head of A and B, respectively. 
Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B 
(yes, B, that's right.); similarly when pB reaches the end of a list, 
redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
"""