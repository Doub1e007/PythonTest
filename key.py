dict1 = {'name':'Tom','age':20,'gender':'male'}

# 1. [key]
# 若当前查找的Key存在 则返回对应的值；否则报错
print(dict1['name'])
# print(dict1['id'])

# 2. 函数
# 2.1 get()
print(dict1.get('name'))
print(dict1.get('names'))  # 若Key不存在，则返回None
print(dict1.get('names','Lily'))  # 若Key不存在，则返回第二个参数 默认是null

# 2.2 keys() # 查找字典中所有的key 返回一个可迭代对象
print(dict1.keys())

# 2.3 values() # 查找字典中所有的key 返回一个可迭代对象
print(dict1.values())

# 2.4 items() # 查找字典中所有的key-value 键值对 返回一个可迭代对象
print(dict1.items())