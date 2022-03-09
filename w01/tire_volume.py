'''
L01 Prove: Milestone (Tire Volume)
'''

import math

#asking the user for measurements
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

#formula
volume = (math.pi * width * width * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/(10000000000)

#the output
print(f'The approximate volume is {volume:.2f}.')
