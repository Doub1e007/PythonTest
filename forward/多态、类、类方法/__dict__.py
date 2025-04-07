# 1.定义类
class A(object):
    a = 0

    def __init__(self):
        self.b = 1

# 2.创建对象
aa = A()

# 3.调用__dict__方法
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)

# 返回实例属性和值组成的字典
print(aa.__dict__)