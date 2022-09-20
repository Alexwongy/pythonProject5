class Restaurant:
    """一个餐厅的营业尝试"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restarant_name,cuisine_type"""
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restarant(self):
        """打印餐厅的名字"""
        print(f'\nThe name of the restauran is {self.restauran_name}!')
        print(f'The cuisine is the following:{self.cuisine_type}')



    def open_restaurant(self):
        print('This restaurant is opening,welcome!')


    def num_served(self):
        """打印这家餐厅已经接待多少人"""
        print(f'This restaurant has served {self.num_served} people.')


restaurant = Restaurant('sichuan', 'mala',)
restaurant.describe_restarant()
restaurant.open_restaurant()
restaurant.num_served()