# Search for x in the list of squares.

sq = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 25
found = False

for i in range(len(sq)):
    if sq[i] == x:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")
