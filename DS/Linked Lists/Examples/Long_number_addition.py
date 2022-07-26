class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
    def str_node(self):
        s = str(self.value)
        if self.next is not None:
            s += self.next.str_node()
        return s

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def print_as_string(self):
        print('Printing linked list as string')
        s=""
        if self.head is not None:
            s+=self.head.str_node()
        print(s)

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

num1="3141592653589793238462643383279502884197169399375105820974944592307816406286"
num2="1414213562373095048801688724209698078569671875376948073176679737990732478462"

#Converting string to Linkedlist
def linked_list(input:str):
    linkedlist=LinkedList()

    for digit in input:
        linkedlist.append_list(int(digit))
    linkedlist.print_as_string() 
    return linkedlist

#Addition
def number_addition(linkedlist1:LinkedList,linkedlist2:LinkedList):
    linkedlist3=LinkedList()

    temp=0

    while(True):
        digit1=linkedlist1.pop_item()
        digit2=linkedlist2.pop_item()
        print(digit1)

        sum=0
        
        if digit1 is None and digit2 is None:
            break
        if digit1 is not None:
            sum+=digit1
        if digit2 is not None:
            sum+=digit2

        sum+=temp

        if sum>9:
            sum=sum-10
            temp=1
        else:
            temp=0
        # print(sum)
        linkedlist3.prepend_node(sum)
    linkedlist3.print_as_string()

linkedlist1=linked_list(num1)
linkedlist2=linked_list(num2)

number_addition(linkedlist1,linkedlist2)

