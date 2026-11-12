# Python program to find prime no in list.

l = [5,1,2,512,51,98756,11217,515,3,25,1,51,14,154,42,2,54,1,54,21,54]

for gh in l:
    while True:
        if gh <= 1:
            print('not prime :',gh)
            
        for op in range(2,gh):
            if gh % op != 0:
                print('it is prime :',gh)
                break
            else:
                print('not prime:',gh)
                break
        break
    
