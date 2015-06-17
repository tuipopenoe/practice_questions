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
            return

    def size(self, node):
        """Return the size of the binary tree."""
        if not node:
            return 0
        else:
            return self.size(node.right) + self.size(node.left) + 1

    def max_depth(self, node):
        """Find the maximum depth of the binary tree."""
        if not node:
            return 0
        else:
            left_height = self.max_depth(node.left)
            right_height = self.max_depth(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def min_value(self, node):
        """Find the minimum value in the binary tree."""
        if not node.left:
            return node.data
        else:
            return self.min_value(node.left)

    def max_value(self, node):
        """Find the maximum value in the binary tree."""
        if not node.right:
            return node.data
        else:
            return self.max_value(node.right)

    def print_tree(self, node):
        """Print inorder traversal of the binary tree."""
        if not node:
            return
        else:
            self.print_tree(node.left)
            print(node.data, end=' ')
            self.print_tree(node.right)

    def print_postorder(self, node):
        """Print postorder traversal of the binary tree."""
        if not node:
            return
        else:
            self.print_tree(node.left)
            self.print_tree(node.right)
            print(node.data, end=' ')

    def print_preorder(self, node):
        """Print preorder traversal of the binary tree."""
        if not node:
            return
        else:
            print(node.data, end=' ')
            self.print_tree(node.left)
            self.print_tree(node.right)

    def print_paths(self, node):
        """Print all the root-to-leaf paths of the binary tree."""
        # TODO

    def mirror(self, node):
        """Mirror the binary tree."""
        if not node:
            return
        else:
            self.mirror(node.left)
            self.mirror(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

    def double_tree(self, node):
        """Insert a duplicate of every node as the left child."""
        if not node:
            return
        else:
            self.double_tree(node.left)
            self.double_tree(node.right)
            temp = node.left
            node.left = Node(node.data)
            node.left.left = temp

    def same_tree(self, node_a, node_b):
        """Return True if both trees are equal, else return False."""
        if not node_a and not node_b:
            return
        elif node_a.data == node_b.data:
            self.same_tree(node_a.left, node_b.left)
            self.same_tree(node_a.right, node_b.right)
        else:
            return False
        return True


class Node(object):
    """Node class in a binary search tree."""
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

