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
        def getsize(node):
            nlen = 0
            while node: nlen += 1; node=node.next
            return nlen

        if not headA or not headB: return None
        alen,blen = getsize(headA),getsize(headB) 
        if alen > blen:
            while alen > blen:
                headA = headA.next; alen -= 1 
        else:
            while blen > alen:
                headB = headB.next; blen -= 1
        while headA:
            if headA == headB: return headA
            headA, headB = headA.next, headB.next 
        return None       

        

if __name__=="__main__":
    l1 = LListUtil.buildList([2,3])
    l2 = LListUtil.buildList([4,5,6])
    l3 = LListUtil.buildList([8,9,10])
    l1.next.next = l3; l2.next.next.next = l3 
    LListUtil.printList(l1); LListUtil.printList(l2); 
    print (Solution().getIntersectionNode(l1,l2)).val

"""
Get both list length, then start to traverse from the shorter length.
e.g.
     a1 -> a2
     |       \
     |         c1 -> c2 -> c3
     |       /            
b1 ->|b2 -> b3
     v
   start point 
"""