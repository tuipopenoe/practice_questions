#/usr/bin/env python
# Tui Popenoe
# Binary Search Tree

class BinarySearchTree(object):
    """Binary Search Tree."""
    def __init__(self, root=None):
        self.root = root

    def lookup(self, node, target):
        """Lookup the target node in the binary tree."""
        if not node:
            return False
        else:
            if target == node.data:
                return True
            else:
                if target < node.data:
                    return self.lookup(node.left, target)
                else:
                    return self.lookup(node.right, target)

    def insert(self, node, data):
        """Insert the given node in the binary tree."""
        if not node:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.left = self.insert(node.right, data)
            return node


class Node(object):
    """Node class in a binary search tree."""
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

