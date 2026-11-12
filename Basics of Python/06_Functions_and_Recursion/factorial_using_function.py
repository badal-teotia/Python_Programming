# WAF to find factorial of n

def factorial(n):
    result = 1
    for s in range(1, n + 1):
        result *= s
    return result

num = int(input("The no is: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(factorial(num))
