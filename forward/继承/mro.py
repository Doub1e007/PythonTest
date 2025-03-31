# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.徒弟类 继承师傅类和学校类 添加和父类同名属性和方法
class Prentice(Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3.用徒弟类创建对象 调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

print(Prentice.__mro__)