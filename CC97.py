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


class Admin(User):
    """管理员特殊用户"""
    def __init__(self,first_name, last_name ):
        """
        初始化父类的属性
        再初始化特有属性
        """
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        """显示管理员权限"""
        msg = f'The Admin has the following right:'
        print(msg)
        if self.privileges:
            for privilege in  self.privileges:
                print(f'\n-self.privileges')

#['can add post', 'can delete post', 'can ban user'

this_user = Admin('alex', 'white')
this_user.privileges = ['can add post', 'can delete post', 'can ban user']
this_user.show_privileges()


