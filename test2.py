# 需求：8位老师 3个办公室 将8位老师随机分配到3个办公室
"""
1.准备数据
    1.1 8位老师名字 --列表
    1.2 3个办公室 --列表嵌套
2.分配老师到办公室
    2.1 随机分配
3.验证是否成功
    打印每个办公室人数和对应老师名字
"""
import random

# 1.准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

# 2.分配老师到办公室 --取到每个老师放到办公室列表 -- 遍历老师列表数据
for name in teachers:
    # 列表追加数据 --append extend insert
    # 随机取到办公室列表的下标
    num = random.randint(0, 2)
    offices[num].append(name)

# print(offices)

# 把各个办公室子列表加一个办公室编号 1 2 3
i = 1
# 3.验证是否成功
for office in offices:
    # 打印办公室人数 -- 子列表数据的个数len()
    print(f'办公室{i}的人数是{len(office)}')
    # 打印办公室老师名字 -- 子列表数据内容
    print(f'办公室{i}老师名字是{office}')
    i += 1






