class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(Master):
    def __init__(self):
        self.kongfu = '现代煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School,self).make_cake()

        # 2.2 无参数super()
        super().__init__()
        super().make_cake()

class Prentice(School):
    def __init__(self):
        self.kongfu = '猫氏煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 子类调用父类的同名方法和属性 把父类同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 需求：一次性调用父类School和Master中的方法
    def make_old_cake(self):
        # 方法一 如果定义的类名修改 这里也要修改 代码量冗余
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二 super()
        # 2.1 super(当前类名,self).函数()
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake()

        # 2.2 无参数super()
        super().__init__()
        super().make_cake()


daqiu = Prentice()

daqiu.make_old_cake()