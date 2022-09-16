prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
 topping = input(prompt)
 if topping != 'quit':
    print(f'I will add {topping} on your pizza')
 else:
     break


