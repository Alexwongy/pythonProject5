#pizza 加上尺寸
# def make_pizzas(size, *toppings):
#     """定义pizza信息的函数"""
#     print(f'\nMaking a {size} inch pizza with the following toppings:')
#     for topping in toppings:
#         print(topping)
#
#
# make_pizzas(4, 'mushrooms')
# make_pizzas(6, 'cheese')


#使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'Gee', location = 'USA', size = 180)
print(user_profile)


