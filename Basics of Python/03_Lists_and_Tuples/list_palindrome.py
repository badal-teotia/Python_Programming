# WAP to check if a list is a palindrome

a = int(input("No: "))
b = int(input("No: "))
c = int(input("No: "))
d = int(input("No: "))
e = int(input("No: "))
f = int(input("No: "))

numbers = [a, b, c, d, e, f]
reverse_numbers = numbers.copy()
reverse_numbers.reverse()

if numbers == reverse_numbers:
    result = "Yes"
else:
    result = "No"

print(numbers)
print("Is the number list a palindrome:", result)
