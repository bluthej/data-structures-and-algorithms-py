from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Implementation(Enum):
    RECURSIVE = 1
    ITERATIVE = 2


@dataclass
class TreeNode:
    """A node of the binary search tree."""

    value: int
    left_child: TreeNode | None = None
    right_child: TreeNode | None = None


@dataclass
class BinarySearchTree:
    """A binary search tree."""

    root: TreeNode

    def insert(self, value: int, impl: Implementation = Implementation.RECURSIVE):
        if impl == Implementation.RECURSIVE:
            self._recursive_insert(value)
        elif impl == Implementation.ITERATIVE:
            self._iterative_insert(value)
        else:
            raise Exception

    def search(self, value: int, impl: Implementation = Implementation.RECURSIVE):
        if impl == Implementation.RECURSIVE:
            return self._recursive_search(value)
        elif impl == Implementation.ITERATIVE:
            return self._iterative_search(value)
        else:
            raise Exception

    def _recursive_insert(self, value: int, ancestor: TreeNode | None = None):
        if ancestor is None:
            ancestor = self.root
        if value > ancestor.value:
            if ancestor.right_child is None:
                ancestor.right_child = TreeNode(value)
            else:
                self._recursive_insert(value, ancestor.right_child)
        else:
            if ancestor.left_child is None:
                ancestor.left_child = TreeNode(value)
            else:
                self._recursive_insert(value, ancestor.left_child)

    def _iterative_insert(self, value: int):
        parent = self.root
        node = parent.right_child if value > parent.value else parent.left_child
        while node is not None:
            parent = node
            node = parent.right_child if value > parent.value else parent.left_child
        if value > parent.value:
            parent.right_child = TreeNode(value)
        else:
            parent.left_child = TreeNode(value)

    def delete(self, value: int):
        current_node = self.root
        parent = None
        # Find the node to delete
        while current_node.value != value:
            if value > current_node.value:
                if current_node.right_child is None:
                    return
                parent, current_node = current_node, current_node.right_child
            else:
                if current_node.left_child is None:
                    return
                parent, current_node = current_node, current_node.left_child
        node_to_delete = current_node

        # If zero or one child, replace with None or only child
        if node_to_delete.left_child is None or node_to_delete.right_child is None:
            if node_to_delete.left_child is None and node_to_delete.right_child is None:
                successor = None
            elif node_to_delete.left_child is None:
                successor = node_to_delete.right_child
            else:
                successor = node_to_delete.left_child
            if node_to_delete == parent.left_child:
                parent.left_child = successor
            else:
                parent.right_child = successor
            return

        # If two children, find the successor node
        successor = node_to_delete.right_child
        parent_of_successor = node_to_delete
        while successor.left_child is not None:
            parent_of_successor, successor = successor, successor.left_child
        node_to_delete.value = successor.value
        if successor == parent_of_successor.right_child:
            parent_of_successor.right_child = None
        else:
            parent_of_successor.left_child = successor.right_child

    def _recursive_search(
        self, value: int, node: TreeNode | None = None
    ) -> TreeNode | None:
        if node is None:
            node = self.root
        if value == node.value:
            return node
        elif value > node.value:
            if node.right_child is None:
                return None
            return self._recursive_search(value, node.right_child)
        else:
            if node.left_child is None:
                return None
            return self._recursive_search(value, node.left_child)

    def _iterative_search(self, value: int) -> TreeNode | None:
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            elif value > node.value:
                node = node.right_child
            else:
                node = node.left_child
        return None
