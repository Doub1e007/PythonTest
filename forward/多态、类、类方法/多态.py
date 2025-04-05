class Dog(object):
    def work(self): # 父类提供统一的方法 哪怕为空方法
        print('指哪打哪...')

class ArmyDog(Dog): # 继承Dog类
    def work(self): # 子类重写父类方法
        print('追击敌人...')

class DrugDog(Dog): # 继承Dog类
    def work(self): # 子类重写父类方法
        print('追查毒品...')

class Person(object):
    def work_with_dog(self, dog): # 接收一个对象
        dog.work() # 对象调用方法

ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad) # 传入一个对象
daqiu.work_with_dog(dd)