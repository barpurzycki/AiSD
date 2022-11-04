from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print( self.data),
        if self.right:
            self.right.print()

    def is_leaf(self) -> bool:
        if TreeNode == None:
            return False
        elif self.right == None and self.left == None:
            return True
        return False

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.add(data)
        else:
            self.data = data


root = TreeNode(5)
root.add(10)
root.add(15)
root.add(12)
root.add(30)
root.print()
