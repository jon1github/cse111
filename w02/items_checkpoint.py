import math

while input != 'quit':
    items = int(input('Enter the number of items (type quit to end the program): '))
    per_box = int(input('Enter the number of items per box: '))

    num_box = math.ceil(items/per_box)

    print(f'For {items} items, packing {per_box} items in each box, you will need {num_box} boxes.')

while input == 'quit':
    print('Goodbye')