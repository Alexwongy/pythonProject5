import json
#如果以前建立了文件，就加载它
#如果还没有，提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('What is you name? ')
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when your come back, {username}!")
else:
    print(f'Welcom back, {username}')