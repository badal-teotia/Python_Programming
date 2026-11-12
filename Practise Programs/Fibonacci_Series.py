# Print fibonacci series.

num = int(input('Terms in fibonacci series :'))

def fibonacci(s):
    a = 0
    b = 1
    print(a)
    print(b)
    count = 0
    while count <= s-3:
        c = a + b
        a, b = b, c
        count += 1
        print(c)

fibonacci(num)
