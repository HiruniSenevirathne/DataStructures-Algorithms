def print_items(a,b):
    for i in range (a):
        print(i)
    # O(a)

    for j in range(b):
        print(j)
    # O(b)

#O(a+b)

def print_items(a,b):
    for i in range (a):
        for j in range(b):
            print(i,j)

# O(a*b)