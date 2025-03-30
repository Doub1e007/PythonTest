# 类：洗衣机 功能:洗衣
class Washer():
    def wash(self):
        print("洗衣服")
        print(self)

haier = Washer()
print(haier)

haier.wash()
# 打印对象和打印self得到的内存地址相同 所以self就是调用该函数的对象