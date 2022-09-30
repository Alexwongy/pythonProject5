def get_formatted_name(first, last, middle = ''):
    """生成整洁的姓名"""
    if middle:
        full_name  = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {middle}"
    return full_name.title()

if __name__ == '__main__':
    print(get_formatted_name('Ali', 'Wong'))


from name_function import get_formatted_name


# print("Enter 'q' at any time to quit")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me the last name: ")
#     if last == 'q':
#         break
#
#
#     format_name = get_formatted_name(last,first) #注意期望结果的语句要与缩进
#     print(f"\tNeatly formatted name: {format_name}.")



