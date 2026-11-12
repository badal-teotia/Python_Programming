# Search for a number x in given tuple.

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
i = 0
found = False

while i < len(num):
    if num[i] == x:
        print("Found at index", i)
        found = True
    i += 1

if not found:
    print("Not found")
