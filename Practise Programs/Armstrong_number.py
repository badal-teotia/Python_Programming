# Check armstrong no.

a = int(input('Give number :'))
b = len(str(a))
c = 0

for digit in str(a):
    c += int(digit) ** b

if c == a:
    print('it is a armstrong number.')
else:
    print('it is not armstrong no.')
