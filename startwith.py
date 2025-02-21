mystr = "hello world and yjsf and albb and Python"

# 1.startwith() 判断字符串是否以某个子串开头
print(mystr.startswith("hello"))
print(mystr.startswith("hel"))
print(mystr.startswith("hels"))

# 2.endswith() 判断字符串是否以某个子串结尾
print(mystr.endswith("Python"))
print(mystr.endswith("python"))

# 3.isalpha() 判断字符串是否只由字母组成
print(mystr.isalpha())

# 4.isdigit() 判断字符串是否只由数字组成
print(mystr.isdigit())

# 5.isalnum() 判断字符串是否只由字母和数字组成
print(mystr.isalnum())

# 6.isspace() 判断字符串是否只由空格组成
mystr1 = ' '
print(mystr1.isspace())