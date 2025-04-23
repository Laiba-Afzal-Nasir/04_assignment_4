# Count Down Timer

import time

def count_down_timer(seconds):
    while seconds > 0 :
        mins, secs = divmod(seconds, 60)   
        time_format = '{:02d}:{:02d}'.format(mins,secs) 
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("00:00 \n Time's Up!\n")

user_input = int(input("\nEnter time in second for countdown: "))
count_down_timer(user_input)