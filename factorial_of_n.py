# WAF to find the factorial of n. (n is the parameter)

def fac(n):
    if(n==1):
        return 1
    return n * fac(n-1)

find = 6
print(fac(find))