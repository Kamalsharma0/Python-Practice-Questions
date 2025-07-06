"""9. Check if a Number is Prime
Question: Write a program to check if a given number, such as 7, is a prime number.
Input: 7
Expected Output: 7 is a prime number
Hint: Prime numbers have no divisors other than 1 and
themselves."""

def primecheck(num):
    is_prime = True
    for i in range(2, int(num/2)):
        if(num%i==0):
            is_prime = False
            break
    return is_prime

print(primecheck(7))