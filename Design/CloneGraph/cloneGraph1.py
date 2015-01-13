#!/usr/bin/python

"""
Clone Graph 

Clone an undirected graph. Each node in the graph contains a label 
and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node 
label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three 
parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus 
forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	if not node: return None
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, v, visited):
        res = UndirectedGraphNode(v.label)
        visited[v.label] = res
        for i in xrange(len(v.neighbors)):
            if v.neighbors[i].label not in visited:
                res.neighbors.append(self.dfs(v.neighbors[i],visited))
            else: 
                res.neighbors.append(visited[v.neighbors[i].label]) 
        return res

if __name__=="__main__":
    node = UndirectedGraphNode(0) 
    print (Solution().cloneGraph(node)).label

"""
Using DFS.
So call clone means deep copy. For this problem, there are two major tasks:
(1)  Traverse the graph.
(2)  Construct the new graph at the same time. 
Same as clone a linked list.
"""
