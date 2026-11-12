# WAP to find factorial of n natural number

n = int(input("Number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial : ", factorial)
