from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.right_child = None
        self.left_child = None

    def is_leaf(self):
        if self.right_child or self.left_child:
            return False
        else:
            return True

    def add_left_child(self, value: Any):
        self.left_child = value

    def add_right_child(self, value: Any):
        self.right_child = value

    def traverse_in_order(self, visit:Callable[[Any], None]):


    def traverse_post_order(self, visit: Callable[[Any], None]):


    def traverse_pre_order(self, visit: Callable[[Any], None]):


    def __str__(self):
        return self.value


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root: 'BinaryNode' = root

    # def traverse_in_order(self, value: Callable[[Any], None]):
    # 
    # def traverse_post_order(self, value: Callable[[Any], None]):
    # 
    # def traverse_pre_order(self, value: Callable[[Any], None]):

    #def show(self):

