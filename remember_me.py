import json


# def greet_user():
#     """问候用户，并指出其名字"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input('What is your name?')
#         with open(filename, 'w') as f:
#             json.dump(username,f)
#             print(f'We will remember you when you come back,{username}!')
#     else:
#         print(f'Welcomeback,{username}!')
#
#
# greet_user()

def get_stored_username():
    """如果存储了用户名，就获取她"""
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
    username = input('What is your name?')
    filename = 'username.json'
    with open(filename) as f:
        json.dump(username, f)
    return username


def greet_username():
    """问候用户，并指出用户名"""
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username()
        print(f'We will remember you when you come back, {username}.')

greet_username()