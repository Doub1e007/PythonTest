name_list = ['TOM','Lily','Jack']

# name_list.append('Lucy')

# name_list.extend('Lucy')
# name_list.extend(['Lucy','Emma'])

name_list.insert(1,'aaa')

print(name_list)

# 1.append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾
# 2.extend函数追加数据的时候如果数据是一个序列，追加序列中的每个元素到列表的结尾
# 3.name_list.insert(下标，数据)