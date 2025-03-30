name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# 1.del
# del name_list
# del (name_list)

# del可以删除指定下标的数据
del(name_list[0])
print(name_list)

# pop() --删除指定下标的数据，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
del_name = name_list.pop(1)
print(del_name)
print(name_list)

# remove(数据)
name_list.remove('David')
print(name_list)

# clear() -- 清空
name_list.clear()
print(name_list)