n = input("Enter the number you want table of this: ")
print(f"The table of {n} will be printed")

try:
    for i in range(1, 11, 1):
        print(f"{n} x {i} = {int(n)*i}")
except ValueError:
    print("Invalid Input")

