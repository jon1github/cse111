from click import prompt
from tools import input_float

def prompt_for_income():
    income = input_float('Please enter your annual income: ')
    return income

def compute_tax(amount):
    return amount * .06

def main():
    print(compute_tax(prompt(prompt_for_income())))

main()