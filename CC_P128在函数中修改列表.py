#创建一个列表，包含一些需要打印的设计
unprinted_designs = ['phone case', 'rpbot pendant', 'dedecahedron']
completed_models = []


#模拟打印每一个设计，智斗没有未打印的设计为止
#打印每个设计后， 都将其地道列表coompled_models中
while unprinted_designs:  #只要列表中没有元素，循环结束
    current_design = unprinted_designs.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)


#显示所有打印好的模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model.title())