#!/usr/bin/python
import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList(arr):
    head = ListNode(0)
    curr = head
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next
    return head.next

def printList(head):
    while head:
        print head.val,
        head = head.next
        if head: print '->',
    print 

def printLists(lists):
        for head in lists:
            while head:
                print head.val,
                head = head.next
                if head: print '->',
            print

def randomArr(ran, num):
    if ran > 0 and num > 0 and ran >= num:
        return random.sample(range(ran),num)