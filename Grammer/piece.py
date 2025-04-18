# 序列名[开始位置下标 :结束位置下标 : 步长]
# 左闭右开区间 步长即间隔 默认为1
str1 = '012345678'
print(str1[2:5:1]) #234
print(str1[2:5:2]) #24
print(str1[2:5]) #234
print(str1[:5]) #01234 不写开始 默认从0开始
print(str1[2:]) #2345678 不写结束 默认到末尾

# 负数测试
print(str1[::-1]) #87654321 步长为负数 表示倒序选取
print(str1[-4:-1]) #567     下标-1表示最后一个数据 依次向前类推

# 终极测试
print(str1[-4:-1:1]) #567
print(str1[-4:-1:-1]) # 不能选出数据：从-4到-1结束，选取方向为从左到右，但是-1步长要求从右到左

