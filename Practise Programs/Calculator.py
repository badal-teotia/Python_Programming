# WAP to create a calculator.

a = float(input('The 1st number is :'))

while True:
    operator_sign = input('Sign (to exit, press enter) :')
    
    if operator_sign == '':
        print('Total',a)
        break
    elif operator_sign not in ('+','*','-','/'):
        print('Invalid input')
        print('Total :',a)
        
    num = float(input('The other number is :'))
    
    if operator_sign == '+':
        a+=num
    elif operator_sign == '-':
        a-=num
    elif operator_sign == '*':
        a*=num
    elif operator_sign == '/':
        a/=num
    elif num == '':
        print('Total',a)