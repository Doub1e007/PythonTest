mystr = "hello world and cast and pdd and Python"

# 1.replace() 把and替换成he  replace()函数有返回值 返回值是修改后的字符串
new_str = mystr.replace('and','he',1)
# 替换次数如果超出子串出现的次数 表示替换所有这个子串
print(mystr)
print(new_str)

# 调用replace()函数后，发现原有字符串的数据并没有修改，修改后的数据是replace的函数返回值
# 说明字符串是不可变数据类型

# 2.split() 分割 返回一个列表 丢失分割字符
list1 = mystr.split('and')
list2 = mystr.split('and',2)
print(list1)
print(list2)

# 3.join() 合并列表里面的字符串数据为一个大字符串
mylist = ['hello','world','and','cast','and','pdd','and','Python']
new_str = '...'.join(mylist)
print(new_str)