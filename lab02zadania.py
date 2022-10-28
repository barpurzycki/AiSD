#Zad 1
from typing import Any

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, value:Any):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def append(self, value:Any):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node

    def insert(self, value:Any, after:None):
        if after is None:
            print("Zły index")
            return

        new_node=Node(value)
        new_node.next=after.next
        after.next=new_node

    def pop(self):
        x = self.head
        if x is not None:
            self.head=x.next
            x = None
            return

    def remove_last(self):
        x = self.head
        while(x.next):
            prev=x
            x = x.next
        prev.next = None

    def remove(self, after:Node):
        if after is None:
            print("Error")
            return
        x = after.next.next
        after.next=x

    def print(self):
        x = self.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data,"-> ", end="")
            x=x.next

    def len(self):
        dl = 0
        x = self.head
        while(x):
            dl+=1
            x = x.next
        return dl

#Zad 2

class Stack:
    def __init__(self):
        self.storage=LinkedList()

    def push(self, element:Any):
        self.storage.push(element)

    def pop(self)->Any:
        self.storage.pop()

    def print(self):
        x = self.storage.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data)
            x = x.next

    def len(self):
        dl = 0
        x = self.head
        while(x):
            dl+=1
            x = x.next
        return dl

#Zad 3

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self):
        return self.storage.head.data

    def enqueue(self, element:Any)->None:
        self.storage.append(element)

    def print(self):
        x = self.storage.head
        while(x):
            if x.next is None:
                print(x.data)
            else:
                print(x.data, ", ", end="")
            x = x.next

    def dequeue(self) -> Any:
        self.storage.pop()

    def len(self):
        dl = 0
        x = self.storage.head
        while (x):
            dl += 1
            x = x.next
        return dl


print("=====================")
list=LinkedList()
list.push(10)
list.push(20)
list.push(40)
list.insert(1,list.head)
list.append(150)
list.print()
list.pop()
list.remove_last()
list.remove(list.head)
list.print()
print("=====================")
stack=Stack()
stack.push(3)
stack.push(10)
stack.push(1)
stack.pop()
stack.push(5)
stack.print()
print("=====================")
queue = Queue()
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue.peek())
queue.print()
queue.dequeue()
print(queue.peek())
queue.print()
print(queue.len())
print("=====================")
