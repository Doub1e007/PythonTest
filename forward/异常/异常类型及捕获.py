# NameError
# print(num)

# ZeroDivisionError
# print(1/0)
"""
try:
    可能发送错误的代码
except 异常类型：
    发生异常时执行的代码
"""
try:
    print(1/0)
except ZeroDivisionError:
    print("除数不能为0")