#!/usr/bin/python

# LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
# following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. 

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        import collections
        self.Dict = collections.OrderedDict()
        self.capacity = capacity
        self.numItems = 0
 
    # @return an integer
    def get(self, key):
        try:
            value = self.Dict[key]
            del self.Dict[key]
            self.Dict[key] = value
            return value
        except:
            return -1
         
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del self.Dict[key]
            self.Dict[key] = value
            return
        except:
            if self.numItems == self.capacity:
                self.Dict.popitem(last = False)
                self.numItems -= 1
            self.Dict[key] = value
            self.numItems += 1
        return

def buildList(lru,arr):
    key = 0
    for i in arr:
        lru.set(key,i)
        key += 1
  
def printLRU(lru):
    if lru.numItems==0: 
        print "empty"
    else:
	for key in lru.Dict.keys():
	    print "<%d,%d>"%(key,lru.Dict[key]),
	print

if __name__=="__main__":
    arr = list(range(10))
    lru = LRUCache(10)
    buildList(lru,arr)
    printLRU(lru)
    lru.get(5)
    printLRU(lru)
    lru.set(1,10)
    lru.set(11,10)
    printLRU(lru)

'''
collections.OrderedDict is a sorted dictionary based on add time order
import collections
a = collections.OrderedDict()
a[1] = 10 # add key-value if key do not exist, otherwise update it.
a.popitem(last = True) # pop the last element
a.popitem(last = False) # pop the first element
'''
