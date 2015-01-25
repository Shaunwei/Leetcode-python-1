#!/usr/bin/python
"""
Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 
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
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head: return None
        curr = ListNode(0)
        curr.next = head
        head = pivot = curr
        while True:
            index = 0
            while pivot and index < k:
                pivot = pivot.next
                index += 1
            if not pivot: return head.next
            else:
                while curr.next != pivot:
                    second = curr.next
                    first = pivot.next
                    curr.next = curr.next.next
                    pivot.next = second
                    second.next = first
                for i in range(k): curr = curr.next 
                pivot = curr
        return head.next

if __name__=="__main__":
    arr = range(1,10)
    head = LListUtil.buildList(arr)
    LListUtil.printList(head)
    LListUtil.printList(Solution().reverseKGroup(head,4))

"""
Simliar as problem 'Swap Nodes in Pairs'.
See an example, we have linked list 3->2->1->4->5->6->7
We wan to reverse 4->5->6 to 6->5->4, so we do the following:
    (1) 3->2->1->4->5->6->7
              p        q
    (2) 3->2->1---->5->6->4->7
              p        q
    (3) 3->2->1------->6->5->4->7
              p        q

The 1st step is to find the locations p and q, where we want to 
reverse from p->next to q.
Then while p->next != q,  we do:
    (1) move p->next to q->next
    (2) connect p->next to p->next->next
Note that, p and q are fixed.
Now we solve this reverse problem, the final step is to scan the whole list:
When we finished one reverse, put p k steps further, set q=p, then put q k 
steps further to find the end node for the new reverse, if meet the end, 
no more reverse needed, return the list.
"""