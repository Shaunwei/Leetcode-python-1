#!/usr/bin/python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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