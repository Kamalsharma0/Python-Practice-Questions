# Write a recursive function to calculate the factorial of a given number n.
# Example: factorial(5) → 120

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    
print(fact(5))