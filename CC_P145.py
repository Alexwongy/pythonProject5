class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()


    def read_odometer(self):
        """打印出一条指出当前汽车里程数的消息"""
        print(f'This car has {self.odometer_reading} miles on it')


    def update_odometer(self, mileage):
        """
        将里程表的读书设置为指定值
        禁止将历程表的读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you can not roll back an odometer!')


    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading += miles


my_used_car = Car('audi', 'a6', '2020')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()