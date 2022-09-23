filename = 'guest_bool.txt'


print("Enter 'quit' when you are finished")
while True:
    name = input("\nWhat is your name?")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as f:
            f.write(f'{name}\n')
        print(f"Hi {name}, you've been add to the guest list")