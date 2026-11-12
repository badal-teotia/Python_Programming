# WAP to identify positive and negative numbers

n = int(input("Give number: "))

if n > 0:
    result = "It is a positive no"
elif n == 0:
    result = "It is zero"
else:
    result = "It is a negative no"

print(result)
