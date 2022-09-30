import json


try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('What is your favorite number?')
    with open('favorite_number.json') as f:
        json.dump(number, f)
    print("Thanks, I will remember that.")
else:
    print(f'I know your favorite number is {number}!')
