#Print menu and hotel counter.(Concession stand program)

food_menu = {'Paratha' : 50,'Ice cream' : 30,'Burger' : 45,'Sandwich' : 50,'Sushi' : 60,'Pizza' : 55,'Haldi': 35}

foods = food_menu.items()

print('-----------MENU-------------')

for key, value in foods:
    print(f'{key:10} : ₹ {value:.1f}')
    
print('-----------------------------')

foods_ordered = []
price = 0

for key, value in foods:
    ask = input('Food item to be ordered ( Q/q to finish ): ')
    
    if ask in food_menu:
        foods_ordered.append(ask)
        price += value
    elif ask.lower() == 'q':
        print('-----------------------------')
        print(f'Total items ordered : {foods_ordered}')
        print(f'Total pricing : ₹ {price}')
        print('Thanks, Your order will arrive soon')
        print('-----------------------------')
        break
    else:
        print ('---Not in menu---')