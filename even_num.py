# Write a Python program to print all even numbers from 1 to 50 using a `continue` statement.

def alleven(start, end):
    for i in range(start, end+1):
        if(i%2!=0):
            continue
        print(i)
        
alleven(1, 50)

    