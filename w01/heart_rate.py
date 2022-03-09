"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65 percent and 85 percent of your heart's maximum rate.
"""

print('When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes.')
age = int(input('How old are you? '))

max_heart_rate = 220 - age
fastest = 0.85 * max_heart_rate
slowest = 0.68 * max_heart_rate

print(f'Your maximum heart rate is {max_heart_rate:.0f}.')

print()

print(f'When exercising to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f}.')