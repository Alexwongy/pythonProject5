def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人个人信息"""
    person = {'first':first_name, 'last':last_name, }
    if age:
        person['age'] = age
    return person

musician = build_person('jimmiy', 'White')
print(musician)
