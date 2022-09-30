#让用户输入一个喜欢的数，编写进文件中，
import json


# number = input('what is your favorite number?')
#
#
# with open('favorite_number.json', 'w') as f:
#     json.dump(number, f)
#     print("Thanks! I'll remember that.")

with open('favorite_number.json') as f:
   number =  json.load(f)

print(f'I know your favorite number, it is {number}')