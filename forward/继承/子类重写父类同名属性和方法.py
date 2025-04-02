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
      self.kongfu = '[独创煎饼果子配方]'
  def make_cake(self):
      self.__init__()
      print(f'运用{self.kongfu}制作煎饼果子')

  # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
  def make_master_cake(self):
      # 父类类名.函数()
      # 再次调用初始化的原因：想要调用父类的同名方法和属性，属性在init初始化位置 所以需要再次调用init
      Master.__init__(self)
      Master.make_cake(self)

  def make_school_cake(self):
      School.__init__(self)
      School.make_cake(self)

# 用徒弟类创建的对象 调用实例属性和方法
daqiu = Prentice()
daqiu.make_cake()

daqiu.make_master_cake()

daqiu.make_school_cake()