# Finding armstrong no in an interval.

il = [5, 6, 156, 4, 65, 75, 844, 1, 153, 1654]

for value in il:
    total = 0
    power = len(str(value))
    
    for digit in str(value):
        total += int(digit) ** power

    if total == value:
        print('is an Armstrong number.', value)
    else:
        print(value, 'is not an Armstrong number.')
