def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

#Woven Squared
#O(n3)=>O(n2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(10)