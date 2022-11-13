from typing import Any, List, Callable, Union
import queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any):
        self.value: value
        self.children: List['TreeNode'] = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        que = queue.Queue()
        for i in self.children:
            que.put(self.children)
        while(queue.qsize(que) > 0):
            visit()




lisc1 = TreeNode(1)
lisc2 = TreeNode(2)
lisc3 = TreeNode(3)
lisc4 = TreeNode(4)
lisc5 = TreeNode(5)
lisc1.add(lisc2)
lisc1.add(lisc3)
lisc2.add(lisc4)
lisc2.add(lisc5)

print(lisc1.is_leaf())
print(lisc2.is_leaf())
print(lisc3.is_leaf())
print(lisc4.is_leaf())
print(lisc5.is_leaf())


