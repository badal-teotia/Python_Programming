# Code to find HCF.

no = int(input('The first no is :'))
n = int(input('The second no is :'))
nu = int(input('The third no is :'))

h = 0

def hcf(no1,no2,no3):
    mini = min(no1,no2,no3)
    for i in range(1, mini+1):
        if no1 % i == 0 and no2 % i == 0 and no3 % i == 0:  
            h = i
    print(h)
             

print('the hcf of these numbers is :-')
hcf(no,n,nu)
