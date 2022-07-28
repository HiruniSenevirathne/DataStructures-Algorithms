from hashlib import new
from multiprocessing import reduction


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    #Append a node
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

    #Pop a node
    def pop(self):
        if self.head is None:
            return None
        temp=self.tail
        self.tail=temp.prev
        self.tail.next=None
        temp.prev=None
        self.length-=1

        if self.length is None:
            self.head=None
            self.tail=None
        return temp.value

    #Prepend a node
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    #Pop first
    def pop_first(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        self.length-=1
        if self.length is None:
            self.head=None
            self.tail=None
        return temp.value

    #Get
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp.value

    #Set
    def set_node(self,index,value):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
                temp.value=value
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
                temp.value=value
        return True
          
    # Another method
    # def set_node2(self,value,index):
    #     temp=self.get(index)
    #     if temp:
    #         temp.value=value
    #         return True
    #     return False

    # Insert
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length-1:
            return self.append(value)

        new_node=Node(value)
        before=self.get(index-1)
        after=before.next

        new_node.prev=before
        new_node.after=after
        before.next=new_node
        after.prev=new_node

        self.length+=1
        return True

    #Remove
    def remove(self,index):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.pop()
        if index==self.length-1:
            return self.pop()

        temp=self.get(index)
     
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None

        self.length-=1
        return temp.value

my_doubly_linked_list=DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.prepend(1)
# my_doubly_linked_list.set_node(1,4)
# # print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.get(2))
print(my_doubly_linked_list.remove(1))

my_doubly_linked_list.print_list()