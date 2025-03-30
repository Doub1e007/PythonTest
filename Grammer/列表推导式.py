# 需求 创建一个0-10的列表
# 1.循环实现 2.列表推导式实现
"""
1.创建空列表
2.循环将有规律的数据写入列表
"""
list1 = []

# while循环实现
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1

# for循环实现
for i in range(10):
    list1.append(i)
print(list1)