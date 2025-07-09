# WAF to print the elements of a list in a single line. ( list is the parameter) using for loop

def print_list(list):
    for i in range(0, len(list)):
        print(list[i], end=" ")


list1 = [1,2,3,5,36,35,36,445,35,236,22] 
print_list(list1)