from Constructor import LinkedList

#Creating Node
class Node:
    def __init__(self,coeff,power):
        self.coeff=coeff
        self.power=power
        self.next=None

    def str_node(self):
            s = "-" if self.coeff<0 else "+" 
            s +=  str(self.coeff) +"X^"+str(self.power) + " " 
            if self.next is not None:
                s += self.next.str_node()
            return s

#Linked Lists' Functions
class polynomial_function:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def print_as_string(self):
        print('Polynomial function : ')
        s=""
        if self.head is not None:
            s+=self.head.str_node()
        print(s)

    def append(self,coeff,power):
        new_node = Node(coeff,power)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head=temp.next
        temp.next=None

        if self.head==None:
            self.tail=None
        self.length -=1
        return temp

#Example Lists
pol1=[[1,2],[2,1],[4,0]]
pol2=[[2,3],[3,2],[4,1],[1,0]]

#Creating Linked Lists
def create_poly_function(input:list):

    linked_list=polynomial_function()

    for term in input:
        linked_list.append(term[0],term[1])
    return linked_list

#Adding Two Polynomials
def poly_add(poly1:polynomial_function,poly2:polynomial_function):
    linked_list_3=polynomial_function()
    term1=poly1.pop_first()
    term2=poly2.pop_first()

    while(True):
        coeff=0
        if term1 is None and term2 is None:
            break

        elif term2 is None or term1.power>term2.power:
            coeff=term1.coeff
            linked_list_3.append(coeff,term1.power)
            term1=poly1.pop_first()

        elif term1 is None or term2.power>term1.power:
            coeff=term2.coeff
            linked_list_3.append(coeff,term2.power)
            term2=poly2.pop_first()

        else:
            coeff=term1.coeff+term2.coeff
            linked_list_3.append(coeff,term1.power)
            term1=poly1.pop_first()
            term2=poly2.pop_first()

    return linked_list_3

poly1=create_poly_function(pol1)
poly2=create_poly_function(pol2)

poly1.print_as_string()
poly2.print_as_string()

#Printing the Output
print("Output ------------------------")
poly3 = poly_add(poly1,poly2)
poly3.print_as_string()

