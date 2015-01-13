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
        newNodes = {node.label : UndirectedGraphNode(node.label)}
        q = []; q.append(node)
        newQ = []; newQ.append(newNodes[node.label])
        visited = set([node]) # A node will be visited as long as it's enqueued
        while q:
            currNode = q.pop(0); newCurrNode = newQ.pop(0)
            for n in currNode.neighbors:
                if n.label not in newNodes:
                    newNodes[n.label] = UndirectedGraphNode(n.label)
                newCurrNode.neighbors.append(newNodes[n.label])
                if n not in visited: 
                    q.append(n); newQ.append(newNodes[n.label])
                    visited.add(n) # A node will be visited as long as it's enqueued
        return newNodes[node.label]

if __name__=="__main__":
    node = UndirectedGraphNode(0) 
    print (Solution().cloneGraph(node)).label

"""
Using BFS.
So call clone means deep copy. For this problem, there are two major tasks:
(1)  Traverse the graph
(2)  Construct the new graph at the same time.
Traverse the graph is similar to the tree traversal, both DFS and  BFS can be used. 
Slight difference  is to consider the loop in the graph (e.g., the 2-->2 in the above figure), 
thus we need store the visited vertex information. If the neighbor of current node 
has not been visited, then search that node.
"""
