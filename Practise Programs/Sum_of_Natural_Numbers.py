# WAP to find sum of natural no.

a = int(input('Number till to find sum :'))
b = 0
c = 0

if a<0:
    print('Please enter a valid natural no. : A positive number')
else:
    while b<=a:
        c += b
        b += 1
        
print(c)
