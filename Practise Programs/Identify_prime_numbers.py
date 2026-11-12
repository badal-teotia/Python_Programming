# Find a program to identify prime no.

temp = int(1)   
num = int(input('The no:'))

while(True): 
    if num <=1:
        print('Not prime')
    if num >1:
        for i in range(2,num):
            if num % i == 0:
                temp = 0
                break
            else:
                continue
    break

if ( temp == 1):
    print('Prime')
else:
    print('Not prime')
    
    