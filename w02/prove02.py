'''
L02 Prove: Milestone (Tire Volume)
'''

import math
from datetime import datetime
current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

#asking the user for measurements
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

#formula
volume = (math.pi * width * width * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/(10000000000)

#the output
print(f'The approximate volume is {volume:.2f}.')

with open('volumes.txt', mode="at") as volumes_file:
    print(f'{current_date_and_time:%d-%m-%Y}, {width}, {aspect_ratio}', file = volumes_file)