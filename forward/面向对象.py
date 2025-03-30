# 需求：洗衣机 功能：洗衣
# 1.创建洗衣机类
"""
class 类名():
    代码
"""
class Washer():
    def wash(self):
        print("洗衣服")

# 2.创建洗衣机对象
# 对象名 = 类名()
haier = Washer()

# 3.验证
#打印haier对象
print(haier)

#使用wash功能 --对象/实例方法 对象名.wash()
haier.wash()