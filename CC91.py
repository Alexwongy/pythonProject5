class Restaurant:
    """一个餐厅的营业尝试"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restarant_name,cuisine_type"""
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restarant(self):
        """打印餐厅的名字"""
        print(f'\nThe name of the restauran is {self.restauran_name}!')
        print(f'The cuisine is the following:{self.cuisine_type}')



    def open_restaurant(self):
        print('This restaurant is opening,welcome!')



my_restaurant = Restaurant('Alex', 'Cheese')
my_restaurant.describe_restarant()
my_restaurant.open_restaurant()


my_restaurant = Restaurant('Chou', 'lamian')
my_restaurant.describe_restarant()
my_restaurant.open_restaurant()


my_restaurant = Restaurant('Sichuan', 'mala')
my_restaurant.describe_restarant()
my_restaurant.open_restaurant()