# Print Even Numbers from 1 to 10
# Question: Write a program to print all even numbers from 1 to 10.
# Expected Output: 2 4 6 8 10
# Hint: Check if a number is even using number % 2 == 0.

def evennum(a, b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
            
evennum(1,10)