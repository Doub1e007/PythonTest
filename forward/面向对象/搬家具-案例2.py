class Furniture():
    def __init__(self,name,area):
        #家具名字
        self.name = name
        #家具占地面积
        self.area = area
# 双人床,6
bed = Furniture('双人床',6)
# 沙发
sofa = Furniture('沙发',10)

class Home():
    def __init__(self,address,area):
        # 房子地址
        self.address = address
        # 房子面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []
    def __str__(self):
        return f'房子坐落于{self.address},面积{self.area}平米,剩余面积{self.free_area}平米,家具列表{self.furniture}'

    def add_furniture(self,item):
        "容纳家具"
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后 房屋剩余面积 = 之前剩余面积 - 家具面积
            self.free_area -= item.area
        else:
            print('剩余面积不足，容纳不下')
# 房子1 北京 1000
jia1 = Home('北京',1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('足球场',2000)
jia1.add_furniture(ball)
print(jia1)

