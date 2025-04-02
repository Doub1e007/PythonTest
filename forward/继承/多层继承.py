class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '现代煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '独创煎饼果子'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 创建徒孙类 用这个类创建对象；用这个对象调用父类的属性和方法
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()

xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_cake()