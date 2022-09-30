nums = []
#输入5个数字
for i in range(5):
    a = input('请输入第' + str(i+1) + '个数字:\n')
    a = int(a)
    nums.append(a)

result = None
for i in range(5):#5个元素，比较5次，
    if result == None:
        result = nums[0]
    elif result > nums[i]:
        result = nums[i]
print('最大值是：', result)
#比较排出最大值
print(max(nums))

