class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[学校煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创版煎饼果子配方]'
        # self.money = 2000000
        # 定义私有属性
        self.__money = 2000000

    # 定义函数：获取私有属性值
    def get_money(self):
        return self.__money

    # 定义函数：修改私有属性值
    def set_money(self):
        self.__money = 50000

    # 定义私有方法
    def info_print(self):
        print('这是私有方法')

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Prentice):
    pass

xiaoqiu = Tusun()

print(xiaoqiu.get_money())

xiaoqiu.set_money()

print(xiaoqiu.get_money())