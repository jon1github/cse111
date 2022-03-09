'''
Can volume, surface area and storage efficiency
'''

import math
def main(radius, height):
    
    print(f'#1 Picnic ')
    print(f'#1 Tall ')
    print(f'#2 ')
    print(f'#2.5 ')
    print(f'#3 Cylinder	')
    print(f'#5 ')
    print(f'#6Z ')
    surface_area = 2 * math.pi * radius * (radius + height)

    volume = math.pi ** radius * height

    storage_efficiency = volume / surface_area
    
main()

