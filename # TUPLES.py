# TUPLES 
## Assignment 1. Creating and Accessing Tuple
### Create a Tuple with first 10 positive integers. Print the Tuple

tuple = (0,1,2,3,4,5,6,7,8,9,10)
print(tuple)
print(type(tuple))

## Assignment 2. Accessing Tuple Elements
### Print the first, middle and last elements of the tuple created in Assignment 1.

number = (0,1,2,3,4,5,6,7,8,9,10)
first, *middle, last = number
print (first)
print (middle)
print (last)

## Assignment 3. Tuple Slicing
### Print the first 3 elements, the last 3 elements and the elements from index 2 to 5 of the tuple created in assignment 1.

number = (0,1,2,3,4,5,6,7,8,9,10)
print(number[0:3])
print(number[-3:])
print(number[2:6])

## Assignment 4. Nested Tuples
### Create a Nested Tuple representing a 3*3 Matrix and print the Matrix. Access and print the element at the second row and third column.


matrix = (
    (1,2,3),
    (4,5,6),
    (7,8,9)

)
print ("Matrix:")
print(matrix)

print("Element of 2nd row, 3rd column")
print(matrix[1][2])

## Assignment 5. Tuple Concatenation
### Concatenete two Tuples: (1,2,3) and (4,5,6). Print the resulting Tuple.

concatenate = (1,2,3)+(4,5,6)
print("Result")
print(concatenate)

## Assignment 6. Tuple Methods
### Create a Tuple with duplicate elements and count the occurances of an element. Find the index of the first occurance of an element in the tuple.

numbers = (1,2,3,2,3,4,5,6)
print("Tuple:", numbers)

print("Count of 2:", numbers.count(2))
print("First index of 2:", numbers.index(2))

## Assignment 7. Unpacking Tuples
### Create a tuple with 5 elements and unpack it into 5 variables. Print the variables

unpacking = (1,2,3,4,5)
a,b,c,d,e = unpacking
print(a)
print(b)
print(c)
print(d)
print(e)

## Assignment 8. Tuple Conversion
### Create a list of the first 5 positive integers to a tuple. Print the tuple.

lst = [1,2,3,4,5]
t = tuple(lst)
print("Tuple:", t)




