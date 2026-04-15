# Set Assignment
## Assignment 1. Creating and Accessing Sets
### Create a Set with the first 10 positive integers. Print the Set.

number = {x+1 for x in range (10)}
print(number)

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

## Assignment 4. Set Comprehensions
### Create a new set containing the squares of the first 10 positive integers using a Set comprehension. Print the new set

squares_set = {x**2 for x in range (1,11)}
print(squares_set)

ordered = sorted({X**2 for X in range (1,11)})
print(ordered)

## Assignment 5. Filtering Sets
### Create a new set containing only the even numbers from the set created in Assignment 1 using a Set comprehension. Print the new set

even_number = {x*2 for x in range (1,11)}
print(even_number)

## Assignment 6. Set Methods
### Create a Set with duplicate elements and remove the duplicates using set methods. Print the modified set

duplicate_elements = {1,2,3,1,2,3,4,5,6,7,8,9,10,6}
print(duplicate_elements)

## Assignment 7. Subsets and Supersets
### Create two sets: One with the first five positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the Results.

Set1 = {1,2,3,4,5}
Set2 = {1,2,3}
print(Set2.issubset(Set1))
print(Set1.issuperset(Set2))

## Assignment 8. Frozenset
### Create a Frozenset with a first 5 positive integers. Print the Frozenset

frozen_numbers = frozenset([1,2,3,4,5])
print(frozen_numbers)

## Assignment 9. Set and List Conversion
### Create a Set with a first five positive integers. Convert it to a List, append the number 6, and convert it back to a Set. Print the Resulting Set

positive_integer = {1,2,3,4,5}
L = list(positive_integer)
L.append(6)
resulting_set = set(L)
print(resulting_set)

## Assignment 10. Set and Dictionary
### Create a Dictionary with Set keys and Integer Values. Print the Dictionary.

dictionary_set = {
    frozenset({1,2}):10,
    frozenset({3,4}):20,
    frozenset({5}):30
}
print(dictionary_set)

## Assignment 11. Iterating over Sets
### Create a Set and Iterate over the elements, printing each element.

iterate_set = {1,2,3,4,5}
for element in iterate_set:
    print(element)

## Assignment 12. Removing Elements from Sets
### Create a Set and remove elements from it until it is empty. Print the Set after each removal.

remove_element = {1,2,3,4,5,6,7}
while remove_element:
    removed_item = remove_element.pop()
    print(f"Removed: {removed_item}")
    print(f"Current_set: {remove_element}")

## Assignment 13. Set Symmetric Difference Update
### Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.

set1 = {1,2,3,5,6,7,8,9}
set2 = {1,2,3,12,13,14,15}
set1.symmetric_difference_update(set2)
print("Modified Set:", set1)

## Assignment 14. Set Membership Testing
### Create a Set and test if certain elements are present in the set. Print the Results

element_set = {1,2,3,4,5,6,7}
print("Is 3 in the Set?", 3 in element_set)
print("Is 10 in the Set?", 10 in element_set)

## Assignment 15. Set of Tuples
### Create a set containing Tuples, where each tuple contains two elements. Print the set.

set_tuple = {(1,2),(3,4),(5,6)}
print(set_tuple)