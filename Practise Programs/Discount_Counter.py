# Making a discount counter for price range.

price = int(input('Price of the item :'))

if price < 499:
    discount = 0
    
elif 999 > price > 499:         #(20 % off)
    discount = price*(1/5)
    
elif 1499 > price > 999:            #(25 % off)
    discount = price*(25/100)
    
elif 2499 > price > 1499:           #(40 % off)
    discount = price*(4/10)
    
else:                             #(50 % off)
    discount = price*(1/2)
    
Total_price = price - discount 

print('--------------------')
print(f'Price : {price}')
print(f'Discount : {discount}')
print(f'Final Price : {Total_price}')
print('--------------------')