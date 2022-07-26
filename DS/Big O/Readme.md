Big O

* Big O is a way of comparing two set of code

Time Complexity
* Number of operations that it takes to complete something.

Space Complexity

Notations in time Complexity
* Omega - Best case scenario
* Theta - Average case
* Omicron - Worst case

Big O
* Always talking about worst case

O(n)
* Propotional

O(n)
* Loop within a loop

O(1)
* Constant
* Most efficient

O(log n)
* Divide and conquer
* Number of items 8 and steps to find a certain number is 3
    2^3=8
    log2 8=3

O(n log n)
* Most efficient in sorting algorithms

Big O: Lists
* O(1) - append/pop last item
         search for a number in a certain index

* O(n) - insert(0,11)/pop(0)
         insert/remove at middle
         Search for a number
         Because we have to re-index

Simplify Big O
* Drop Constants
* Can't do if a function has two different parameters
    O(2n) => O(n)

* Woven Squared
    o(n3) => O(n2)

* Drop Non-Dominants
    O(n2 + n ) => O(n2)