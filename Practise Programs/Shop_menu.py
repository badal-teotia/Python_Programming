# Shop menu shopping manual.

food = []
price = []
total = 0

print('-------WELCOME TO THE SHOP-------')
print('___Place your order___')

while True:
    th = input('Item ("q to go to cart") :')
    if th.lower() == 'q':
        break
    else:
        he = float(input('Item price (In Rupee) :'))
        food.append(th)
        price.append(he)
        total += he
print(food)
print(price)
print('Total pricing :',total,'Rupee')