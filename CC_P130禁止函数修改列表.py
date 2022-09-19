# 保留原来的列表以供备案
#可以通过想函数列表传递列表的副本而不是原件，这样任何修改都只影响副本

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每一个设计，知道没有未打印的设计为之。
    打印每个设计后，都将其移动到列表completed_models
    """
    while unprinted_designs: #+


        current_design = unprinted_designs.pop()
        print(f'Printing model:{current_design}')
        completed_models.append(current_design)


def show_compled_models(completed_models):
    """显示打印好的所有模型"""
    print('\nPrinting the following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dedecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) #unprinted_designs函数的全称里面写 后面加上[:]  ，表示从开始到最后一个元素，但是调用的列表的副本，原件不受影响
show_compled_models(completed_models)
print(unprinted_designs)
#为什么说效率更高，因为定义了两个函数之后，只需要提供未打印的设计名单，全部看出来
