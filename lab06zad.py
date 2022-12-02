from typing import Any

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def min(self, BinaryNode):
        wart = BinaryNode
        while wart.left_child is not None:
            wart = wart.left_child

        return wart.value

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root):
        self.root: 'BinaryNode' = root

    def insert(self, value: Any) -> None:
        
    # def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
    #
    # def insert_list(self, list_: List[Any]) -> None:
    #
    # def contains(self, value: Any) -> bool:
    #
    # def remove(self, value: Any) -> None:
    #
    # def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
    #
    # def show(self):
