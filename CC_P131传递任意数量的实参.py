# def make_pizza(*toppings):   #*创建名为topping的空元祖
#     """打印顾客的所有配料"""
#     print(toppings)
#
# make_pizza('peperoni')
# make_pizza('mushrooms', 'cheese', 'green peppers')


def make_pizzas(*toppings):
    """概述要制造的pizza"""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizzas('pepperoni')
make_pizzas('mushroons', 'green peppers', 'cheese')
