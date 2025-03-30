mystr = "hello world and python and me"

# 1.find()
print(mystr.find('and')) # 12
print(mystr.find('and',15,30)) # 23
print(mystr.find('ands',15,30)) # ands子串不存在

# 2.index()
print(mystr.index('and')) # 12
print(mystr.index('and',15,30)) # 23
# print(mystr.index('ands',15,30)) # 子串不存在 报错

# 3.count()
print(mystr.count('and',15,30)) # 1
print(mystr.count('and')) # 2
print(mystr.count('ands')) # 0

# 4.rfind() 从右侧开始查找
print(mystr.rfind('and')) # 23
print(mystr.rfind('ands'))

# 5.rindex()
print(mystr.rindex('and')) # 23


