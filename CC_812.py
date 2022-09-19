#做不同用料的三明治
def make_sandwiches(*ingredients):
    """做一个选择三明治用料的函数"""
    print('\nwhat would you like in your sandwich?')
    print(f"-{ingredients}")


make_sandwiches('cheese', 'pork', 'tomatos', 'egg')
make_sandwiches('cheese', 'pork')
make_sandwiches('cheese')


#为什么这里将每个用料都打印了几次，去掉for语句就没有了，为什么