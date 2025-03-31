# 定义Init魔法方法 设置初始化属性并访问
"""
1.定义类
    魔法方法init width和height
    添加实例方法 访问实例属性
2.创建对象
3.验证
    调用实例方法
"""
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 400
        self.height = 500

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier1 = Washer()

haier1.print_info()