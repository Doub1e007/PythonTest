"""
for 临时变量 in 序列:
    代码块
"""

str1 = 'hello world'
for a in str1:
    # 当某些条件成立退出循环 --break 条件 i取到r
    if a == 'r':
        continue
       # break
    print(a, end=' ')