# WAF to find factorial using recursion

i = int(input("The no: "))

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

if i < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(fact(i))
