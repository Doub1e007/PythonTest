# 1.定义类：初始化属性 方法 显示对象信息str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 状态
        self.cook_state = "生的"
        #调料列表
        self.condiments = []

    def __str__(self):
        return f"地瓜被烤了{self.cook_time}分钟，状态是{self.cook_state}，调料有{self.condiments}"

    def cook(self, time):
        "烤地瓜的方法"
        # 1.计算地瓜整体烤过的时间
        self.cook_time += time
        # 2.根据烤过的时间，判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_state = "生的"
        elif 3 <= self.cook_time < 5:
            self.cook_state = "半生不熟"
        elif 5 <= self.cook_time < 8:
            self.cook_state = "熟透"
        elif self.cook_time >= 8:
            self.cook_state = "糊了"

    def add_condiments(self, condiment):
        "用户意愿的调料追加到调料列表"
        self.condiments.append(condiment)

# 2.创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)

digua1.cook(4)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)
digua1.add_condiments('孜然')
print(digua1)