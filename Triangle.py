"""
打印一个三角形
每行星星的个数和行号相等
"""
j = 0
while j < 5:
    i = 0
    while i <= j:
        print("*", end="")
        i += 1
    print()
    j += 1