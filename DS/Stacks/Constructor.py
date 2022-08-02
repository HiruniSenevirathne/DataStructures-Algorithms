from tkinter import N


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.lenght=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    #Push
    def push(self,value):
        new_node=Node(value)

        if self.top is None:
            self.top=new_node
            self.next=None
        else:
            new_node.next=self.top
            self.top=new_node
        self.lenght+=1
    #Pop
    def pop(self):
        if self.lenght==0:
            return None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        self.lenght-=1

my_stack=Stack(4)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()

