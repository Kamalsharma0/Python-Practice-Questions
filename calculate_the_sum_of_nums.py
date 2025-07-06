"""4. Calculate Sum of Numbers from 1 to 10
Question: Write a program to calculate the sum of numbers
from 1 to 10.
Expected Output: Sum = 55
Hint: Initialize a variable for the sum and add each number in the loop."""

def sum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    print(f"The sum from {a} to {b} = {sum}")

sum(1,10)