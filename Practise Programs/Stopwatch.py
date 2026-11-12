#  Countdown timer.

import time

gh = int(input('Time in second :'))

for x in range(gh,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600) % 60
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)
    
print("Time's up man")
