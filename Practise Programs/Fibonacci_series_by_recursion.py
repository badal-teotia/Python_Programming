# To print fibonacci series by recursion.

def fibo (r):
    if r <= 1:
        return r
    else:
        return fibo(r-1) + fibo(r-2)
    
place = int(input('Terms to be in series:'))

if place < 0:
    print('The number given is invalid')
else :
    print('The fibonacci series is :-')
    for i in range(place):
        print(fibo(i))