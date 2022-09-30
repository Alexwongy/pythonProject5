#统计出现次数最多的字母
# string1 = 'goJavaPythonPHP'
# #转换小写
# string1 = string1.lower()
# #定义一个字典
# letter = {}
# #记录字母出现的次数
# for char in string1:
#     if char not in letter.keys():
#         letter[char] = 1
#     else:
#         letter[char] += 1
# print(letter)


string1 = 'WhenwillYouleave'
string1 = string1.lower()
letters = {}
for char in string1:
    if char not in letters.keys():
        letters[char] = 1
    else:
        letters[char] += 1
count = max(letters.values())
for key, value in letters.items():
    if value == count:
        print(key)