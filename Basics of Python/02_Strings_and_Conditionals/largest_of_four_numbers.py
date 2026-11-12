# WAP to identify the largest no of the 4 given no

n1 = int(input("1st no: "))
n2 = int(input("2nd no: "))
n3 = int(input("3rd no: "))
n4 = int(input("4th no: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    result = "n1 is big"
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    result = "n2 is big"
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    result = "n3 is big"
else:
    result = "n4 is big"

print("Largest no:", result)
