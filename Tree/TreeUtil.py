#!/usr/bin/python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildLeetTree(arr):
    if len(arr)==0 or arr[0]=='#': return None
    alen, nodes, nidx = len(arr), [], 0
    for i in arr:
        if i == '#': nodes.append(None)
        else: nodes.append(TreeNode(i))
    for index in range(alen/2):
        if 2*index+1 < alen:
            if not nodes[index]:
                nidx = index
                while not nodes[nidx] and nidx<alen:
                    nidx += 1
                nodes[nidx].left = nodes[2*index+1]
            elif nidx > 0: nodes[nidx].left = nodes[2*index+1]
            else: nodes[index].left = nodes[2*index+1]
        if 2*index+2 < alen:
            if nidx > 0:
                nodes[nidx].right = nodes[2*index+2]
                nidx += 1
            else: nodes[index].right = nodes[2*index+2]
    return nodes[0]

def buildTree(arr):
    if len(arr) == 0: return None
    nodes = []
    for i in arr:
        nodes.append(TreeNode(i))
    for index in range(len(arr)/2):
        if 2*index+1 < len(arr):
            nodes[index].left = nodes[2*index+1]
        if 2*index+2 < len(arr):
            nodes[index].right = nodes[2*index+2]
    return nodes[0]

def buildTreeInOrder(arr):
    if len(arr) == 0: return None
    root = TreeNode(arr[0])
    for i in arr[1:]:
        orderInsert(root,i)

    return root

def orderInsert(root, data):
    # it there isn't any data and add it
    if root == None:
        return TreeNode(data)
    else:
        if data <= root.val:
            root.left = orderInsert(root.left, data)
        else:
            root.right = orderInsert(root.right, data)
        return root

def print_tree_in(node):
    if node == None:
        pass
    else:
        print_tree_in(node.left)
        print node.val, 
        print_tree_in(node.right)       

def print_tree_pre(node):
    if node == None:
        pass
    else:
        print node.val,
        print_tree_pre(node.left)      
        print_tree_pre(node.right)

def print_tree_pos(node):  
    if node == None:
        pass 
    else: 
        print_tree_pos(node.left)      
        print_tree_pos(node.right)
        print node.val, 

def print_tree_level(node):  
    if not node: return
    q = [node]
    while q:
        node = q.pop(0)
        print node.val,
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

def print_tree(node, order):
    if node:
        if order == 'pre-order': print node.val,
        print_tree(node.left, order)
        if order == 'in-order': print node.val,
        print_tree(node.right, order)
        if order == 'post-order': print node.val,

def print_tree_graph(node):
    maxLvl = maxLevel(node)
    printNodeInternal([node], 1, maxLvl)

def printNodeInternal(nodes, level, maxLevel):
    if not nodes or isAllNull(nodes): return
    floor = maxLevel - level
    endgeLines = 2 ** max(floor-1, 0)
    firstSpaces = 2 ** floor - 1
    betweenSpaces = 2 ** (floor+1) - 1
    printWhitespaces(firstSpaces)
    newNodes = []
    for node in nodes:
        if node:
            print node.val,
            newNodes.append(node.left)
            newNodes.append(node.right)
        else:
            newNodes.append(None)
            newNodes.append(None)
            print ' ',
        printWhitespaces(betweenSpaces)
    print
    for i in xrange(1,endgeLines+1):
        for j in xrange(len(nodes)):
            printWhitespaces(firstSpaces-i)
            if not nodes[j]:
                printWhitespaces(endgeLines+endgeLines+i+1)
                continue
            if nodes[j].left: print '/',
            else: printWhitespaces(1)
            printWhitespaces(i+i-1)
            if nodes[j].right: print '\\',
            else: printWhitespaces(1)
            printWhitespaces(endgeLines+endgeLines-i)
        print
    printNodeInternal(newNodes, level+1, maxLevel)

def printWhitespaces(count):
    for i in xrange(count):
        print ' ',

def maxLevel(node):
    if not node: return 0
    return max(maxLevel(node.left), maxLevel(node.right)) + 1

def isAllNull(alist):
    for elment in alist:
        if elment: return False
    return True

"""
Pre-order:
Visit the root.
Traverse the left subtree.
Traverse the right subtree.

In-order (symmetric):
Traverse the left subtree.
Visit the root.
Traverse the right subtree.

Post-order:
Traverse the left subtree.
Traverse the right subtree.
Visit the root.
"""