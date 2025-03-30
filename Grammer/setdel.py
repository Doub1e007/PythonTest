s1 = {10,20, 30, 40, 50}

# remove():删除指定数据 数据不存在报错
s1.remove(30)
print(s1)

# s1.remove(30)
# print(s1)

# discard():删除指定数据 数据不存在不报错
s1.discard(10)
print(s1)

# pop():随机删除一个数据
del_num = s1.pop()
print(del_num)
print(s1)