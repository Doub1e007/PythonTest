class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'使用{self.kongfu} 制作煎饼果子')

# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[学校煎饼果子配方]'
    def make_cake(self):
        print(f'使用{self.kongfu} 制作煎饼果子')

# 一个类有多个父类的时候 默认使用第一个父类同名属性和方法
class Prentice(School,Master):
    pass

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()