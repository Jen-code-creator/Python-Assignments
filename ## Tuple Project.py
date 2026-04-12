## Tuple Project

## Assignment 8. Tuple Conversion
### Create a list of the first 5 positive integers to a tuple. Print the tuple.

lst = [1,2,3,4,5]
t = tuple(lst)
print("Tuple:", t)

## Assignment 9. Tuple of Tuples
### Create a Tuple containing 3 Tuples, each with 3 elements. Print the type of Tuples.

number = ((1,2,3), (4,5,6), (7,8,9))
print(type(number))

## Assignment 10. Tuple and List
### Create a Tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a Tuple. Print the resulting Tuple.

number = (1,2,3,4,5)
L = list(number)
L.append(6)
T= tuple(L)
print("Result:", T)

## Assignment 11. Tuple and String
### Create a Tuple with a character of a string. Join the Tuple elements into a single string. Print the string.

text = "hello"
t=tuple(text)
print("Tuple:", t)

result = ''.join(t)
print("String:", result)

## Assignment 12. Tuple and Dictionary
### Create a Dictionary with Tuple Keys and integer Values. Print the dictionary.

d = {
    (1,2):10,
    (3,4):20,
    (5,6):30
}
print(d)

## Assignment 13. Nested Tuple Iteration
### Create a Nested Tuple and iterate over the elements, printing each elements.

nested = ((1,2,3), (4,5,6), (7,8,9))

for i in nested:
    for j in i:
        print(j)

for row in nested:
    print(row)

## Assignment 14. Tuple and Set
### Create a Tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.

numbers = (1,2,3,1,2,3,4,5,6,7)
s = set(numbers)
print("Result:", s)

## Assignment 15. Tuple Functions
### write function that take a Tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

def analyze_tuple(t):
    minimum = min(t)
    maximum = max(t)
    total = sum(t)
    return minimum, maximum, total

numbers = (1,2,3,4,5)
result = analyze_tuple(numbers)

print("Minimum:", result[0])
print("Maximum:", result[1])
print("Total:", result[2])

