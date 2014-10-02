#!/usr/bin/python

# LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
# following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. 

# define the double linked list, each node stores both the key and value.
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


# implimentation using hashmap with double linked-list
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = None
    	self.tail = None
    	self.mapnode = {}
    	self.capacity = capacity

    # insert node to the tail of the linked list
    def insertNode(self, node):
    	if not self.head:
    	    self.head = node
    	    self.tail = node
    	else:
    	    self.tail.next = node
    	    node.prev = self.tail
    	    self.tail = self.tail.next
    
    # remove current node
    def removeNode(self, node):
    	if node == self.head:
    	    self.head = self.head.next
    	    if self.head:
    	    	self.head.prev = None
        else:
    	    if node == self.tail:
    	    	self.tail = self.tail.prev
    	    	self.tail.next = None
    	    else:
    	    	node.next.prev = node.prev 
    	    	node.prev.next = node.next 

    # move current node to the tail of the linked list
    def moveNode(self, node):
        if node == self.tail:
    	    return
        else:
            if node == self.head:
    	        node.next.prev = None 
    	        self.head = node.next 
    	        self.tail.next = node 
    	        node.prev = self.tail 
    	        self.tail = self.tail.next 
    	        self.tail.next = None 
            else:
		node.next.prev = node.prev 
		node.prev.next = node.next 
		self.tail.next = node 
		node.prev = self.tail 
		self.tail = self.tail.next 
		self.tail.next = None 
    
    def get(self, key):
        if key not in self.mapnode:
            return -1 
        else:
            self.moveNode(self.mapnode[key]) 
            return self.mapnode[key].val 
         
    def set(self, key, value):
        if key in self.mapnode: 
            self.moveNode(self.mapnode[key]) 
    	    self.mapnode[key].val = value 
    	else: 
    	    if len(self.mapnode) == self.capacity: 
    	        del self.mapnode[self.head.key] 
    	    	self.removeNode(self.head) 
            node = Node(key,value)
    	    self.mapnode[key] = node
    	    self.insertNode(node) 
									
    def printLRU(self):
    	curr = self.head 
    	while curr: 
    	    print "<%d,%d>"%(curr.key,curr.val),
    	    curr = curr.next 
    	print

    def buildList(self, arr):
	for i in arr:
	    self.set(i,i)
           
if __name__=="__main__":
    arr = list(range(10))
    lru = LRUCache(10)
    lru.buildList(arr)
    lru.printLRU()
    lru.get(5)
    lru.printLRU()
    lru.set(0,10)
    lru.set(11,11)
    lru.printLRU()
     
 

