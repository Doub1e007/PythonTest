# 1-100偶数累加和 -- 2 + 4 + 6 + ... + 100
"""
1.准备要累加的数字
2.准备保存结果的变量
3.循环累加
4.输出结果
"""
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
     result += i
    i += 1
print(result)