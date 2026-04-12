# Set Assignment
## Assignment 1. Creating and Accessing Sets
### Create a Set with the first 10 positive integers. Print the Set.

number = {0,1,2,3,4,5,6,7,8,9,10}
print(type(number))

## Assignment 2. Adding and Removing Elements
### Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.

number = {0,1,2,3,4,5,6,7,8,9,10}
number.add(11)
number.remove(1)
print(number)

## Assignment 3. Set Operations
### Create two sets: One with the first five positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

set1 = {1,2,3,4,5}
set2 = {2,4,6,8,10}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Difference (set2 - set1):", set2 - set1)
print("Symmetric Difference:", set1 ^ set2)