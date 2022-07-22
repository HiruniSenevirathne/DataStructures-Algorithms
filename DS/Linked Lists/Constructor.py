#Creating a new node
from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node =Node(value)
        self.head=new_node 
        self.tail=new_node
        self.length=1

    #Print List
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    #Append a node
    def append_list(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
    
    #Pop a node
    def pop_item(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value

    #Prepend a Node
    def prepend_node(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    #Pop First
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    #Get
    def get(self,index):
        if index<0 or index>self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    #Set
    def set_item(self,index,value):
        if self.length==0:
            return None
        if index<0 or index>self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        if temp:
            temp.value=value
            return True
        return False
    #def set_item(self,index,value):
        # temp=self.get(index)
        # if temp:
        #     temp.value=value
        #     return True
        # return False

    #Insert
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend_node(value)
        if index==self.length:
            return self.append_list(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    #Remove
    def remove(self,index):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.pop_first()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        if index==self.length-1:
            return self.pop_item()
        return temp



my_linked_list=LinkedList(1)
my_linked_list.append_list(2)
my_linked_list.append_list(3)
# my_linked_list.print_list()
# print(my_linked_list.get(2))

# my_linked_list.prepend_node(3)
# print("********")
# my_linked_list.print_list()

# print(my_linked_list.pop_item())
# print(my_linked_list.pop_item())
# print(my_linked_list.pop_item())

# print(my_linked_list.pop_first())
print(my_linked_list.remove(2),'\n')

my_linked_list.set_item(2,4)
my_linked_list.print_list()

