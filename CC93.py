class User:
    """存储用户信息的类"""
    def __init__(self, first_name, last_name):
        "初始化User的属性"
        self.first_name = first_name
        self.last_name = last_name


    def describe_user_info(self):
        """打印用户信息"""
        print(f'The user name is {self.first_name.title()} {self.last_name.title()} ')


    def greet_user(self):
        """向用户发出问候"""
        print(f'Hello,{self.first_name.title()} {self.last_name.title()} !')


this_user = User('alex', 'white')
this_user.describe_user_info()
this_user.greet_user()