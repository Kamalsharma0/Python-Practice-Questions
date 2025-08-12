num1 = int(input("a: "))
num2 = int(input("b: "))

while (num2!=0):
    num1, num2 = num2, num1%num2

print(num1)