DSA = Data Structures and Algorithms

Think of it like:

Data Structure = How data is stored

Algorithm = Steps to solve a problem

Example:

You have numbers:

[10, 5, 30, 20]

Question:

Which number is largest?

Finding the largest number is an algorithm.


  ex:::


numbers = [10, 5, 30, 20]
largest=numbers[0]
for x in numbers:
    if x > largest:
        largest=x
print(largest)
