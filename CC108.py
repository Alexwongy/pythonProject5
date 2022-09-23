# cat_name = 'cats.txt'
#
#
# with open(cat_name, 'w') as cat_object:
#     cat_object.write('mimi\n')
#
#
# with open(cat_name, 'a') as cat_object:
#     cat_object.write('maomao\n')
#     cat_object.write('miumiu\n')
#
#
# dog_name = 'dogs.txt'
# with open(dog_name, 'w') as f:
#     f.write('wangcai\n')
#     f.write('facai\n')
#     f.write('wangwang\n')

filenames = ['cats.txt', 'dogs.txt']


for filename in filenames:
    print(f'\nReading file: {filename}')
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print('Sorry, I can not find that file')
