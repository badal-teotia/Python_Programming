# Find the largest among 3 no.

a = float(input('enter num 1:'))
b = float(input('enter num 2:'))
c = float(input('enter num 3:'))

if a>b and a>c:
    print('Largest no is :',a)
elif b==a and b>c:
    print('Largest no are',a, 'and',b)
elif b>a and b>c:
    print('Largest no is :',b)
elif a==b==c:
    print('All no are equal.')
elif b>a and b==c:
    print('Largest no are', b, 'and', c)
else:
    print('Largest no is :',c)
    
    