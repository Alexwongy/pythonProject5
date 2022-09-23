from CC96 import Restaurant


hao_chi= Restaurant('Sichuan', 'MaPoDouFu')  #表格把额外添加的属性写到这里
hao_chi.flavors = ['mala', 'xiangchao', 'heizhima']#新开一个重新写，实例.功能名（函数名）
hao_chi.describe_restaurant()  #实例.方法
hao_chi.open_restaurant()
hao_chi.number_served = 10  #实例.属性 = 实际数值
print(f'There are {hao_chi.number_served} people in the restaurant')
#原函数里面没有print的话，就不会打印出来，要自己print，f''和{}搭配使用
# from CC96 import IceCreamStand:


#类的命名要驼峰法，不用下划线， class 后面那个
#实例名和模块名用小写+下划线，