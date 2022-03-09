import math

def main():
    most_cost_efficient = 0
    most_storage_efficient = 0
   
    cans = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73,11.59,0.45],
        ["#2.5", 10.32, 11.91, 0.43],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6z", 5.40, 8.89, 0.22],
        ["#8z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 7.62, 0.26],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

    for name, radius, height, cost in cans:
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        print(f'{name} {storage_efficiency:.1f} {cost_efficiency:.0f}')

        if most_cost_efficient < cost_efficiency:
            most_cost_efficient = cost_efficiency
        elif most_storage_efficient < storage_efficiency:
            most_storage_efficient = storage_efficiency
    
    print()
    print(f'The can size with the best storage efficiency is {most_storage_efficient:.1f}')
    print(f'The can size with the best cost efficiency is {most_cost_efficient:.0f}')



def compute_volume(radius, height):
    volume = (math.pi)*(radius**2)*(height)
    return volume

def compute_surface_area(radius, height):
    surface_area = (2*math.pi)*(radius)*(radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost
    return cost_efficiency

main()