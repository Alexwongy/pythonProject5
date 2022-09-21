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
        """显示一条消息，餐厅正在营业"""
        msg = f'This restaurant is opening,welcome!'
        print(msg)


    def num_served(self):
        """打印这家餐厅已经接待多少人"""
        print(f'This restaurant has served {self.num_served} people.')

    def set_num_served(self, num_served):
        """让用户能够设置就餐人数"""
        self.num_served = num_served
        print(f'There are {num_served} in the restaurant')




restaurant = Restaurant('sichuan', 'mala') #num_served = 10 不能写在此处
restaurant.describe_restarant()
restaurant.open_restaurant()
restaurant.set_num_served(10)