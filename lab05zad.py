from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.right_child = None
        self.left_child = None

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        else:
            return True


    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)

        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return self.value


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root: 'BinaryNode' = root

    def traverse_in_order(self, value: Callable[[Any], None]):
       self.root.traverse_in_order(value)
    def traverse_post_order(self, value: Callable[[Any], None]):
       self.root.traverse_post_order(value)
    def traverse_pre_order(self, value: Callable[[Any], None]):
        self.root.traverse_pre_order(value)



