class Restaurant():
    """一个表示餐馆的类。"""
    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")
