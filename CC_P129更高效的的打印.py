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

print_models(unprinted_designs, completed_models)
show_compled_models(completed_models)

#为什么说效率更高，因为定义了两个函数之后，只需要提供未打印的设计名单，全部看出来
