"""8. Calculate Factorial of a Number
Question: Write a program to calculate the factorial of a given number, such as 5.
Input: 5
Expected Output: 120
Hint: Multiply each number from 1 to the given number."""

def fac(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    print(factorial)
    
fac(5)
