# WA function to sum the first n natural no

i = int(input("The natural no: "))

def s(n):
    if n == 0:
        return 0
    else:
        return n + s(n - 1)

if i < 0:
    print("Please enter a non-negative number.")
else:
    print(s(i))
