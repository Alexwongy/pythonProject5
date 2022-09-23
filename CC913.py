#创建一个Die的类，包含一个sides的属性，该属性的默认值为6，
#编写一个名为roll_die()的方法，打印位于和骰子面之间的随机数
#创建一个6面的骰子再掷10次
from random import randint


class Die:
    """创建一个Die的类"""
    def __init__(self, sides = 6):
        """初始化Die的属性"""
        self.sides = sides


    def roll_die(self):
        """编写roll_die的方法，打印位于1和骰子面之间的随机数"""  #这里该如何实现
        return randint(1,self.sides)


#创建一个6面的骰子，再扔10次并显示结果
d6 = Die()


results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print('10 rolls of a 6-sides die:')
print(results)

#创建10面的骰子，扔10次并显示结果
# d10 = Die(sides = 10)
#
#
# results = []
# for roll_num in range(10):
#     result = d10.roll_die()
#     results.append(result)
# print('\n10 rolls of a 10-side die:')
# print(results)

#创建20面的骰子，扔10次显示结果
d20 = Die(sides = 20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print('\n10 roll of a 20-sided die:')
print(results)