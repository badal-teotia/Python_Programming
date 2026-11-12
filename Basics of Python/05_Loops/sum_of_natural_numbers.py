# WAP to find sum of first n natural numbers.

n = int(input("No till which to find sum: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Total sum:", total)
