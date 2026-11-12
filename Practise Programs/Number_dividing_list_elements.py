# WAP to display numbers in list divisible by another no.

li = [1,2,3,4,5,6,7,8,9,35,72,84,91,46,47,13,29,50]

num = int(input('No to divide :'))

print('the no divisible by',num ,'is/are :-')
for c in li:
    if c % num ==0:
        print(c)
    else:
        continue 
