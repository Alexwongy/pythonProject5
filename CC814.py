def make_car(manufacturer, model, **options):
 """创建一个表示汽车的字典。"""
 car_dict = {
 'manufacturer': manufacturer.title(),
 'model': model.title(),
 }
 for option, value in options.items():
  car_dict[option] = value
  return car_dict


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
 headlights='popup')
print(my_old_accord)