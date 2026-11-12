# To make a shop list maker.

print("------Menu------")
print("Pizza     = 30")
print("Ice cream = 15")
print("Paratha   = 20")
print("Burger    = 40")

foods = []
prices = []
cost = 0

while True:
    f = input("Food item to be ordered ('q' to finish order):")
    
    if f == 'Pizza':
        foods.append('Pizza')
        prices.append(30)
        cost += 30
        
    elif f == 'Ice cream':
        foods.append(f)
        prices.append(15)
        cost += 15
        
    elif f == 'Paratha':
        foods.append(f)
        prices.append(20)
        cost += 20
        
    elif f == 'Burger':
        foods.append(f)
        prices.append(40)
        cost += 40
        
    elif f == 'q':
        print('Items ordered',foods)
        print('Total :',cost,'Rupees')
        print('Thanks for coming, Please visit again.')
        break
    
    else:
        print('NOT IN MENU_________!!!!!')
