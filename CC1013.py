import  json


def get_stored_username():
    """获取存储用户——如果存储了"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示输入用户名"""
    username = input("what is your name")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """基于用户名问候用户"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n)")
        if correct == 'y':
            print(f'Welcome back, {username}')
        else:
            username = get_new_username()
            print(f"We'll remember you when you come backm, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come backm, {username}")




greet_user()

#假设用户要么已经输入用户名，要么是首次运行程序
#设置的程序要防止当前的用户不是上一次运行的用户
#username.json 有且只有一个用户名