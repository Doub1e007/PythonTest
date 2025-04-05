# 1.自己的文件名不能和已有模块名重复 如果重复导致模块无法使用 --random
# import random
# num = random.randint(1,5)
# print(num)

# 2.当使用from xx import 功能 导入模块功能的时候 如果功能名字重复 导入的时候定义或后导入的这个同名功能
# 场景 time.sleep()
def sleep():
    print("自定义的sleep函数")

from time import sleep

# 定义函数 sleep
# def sleep():
#     print("自定义的sleep函数")
sleep(2)

# 名字重复
# import