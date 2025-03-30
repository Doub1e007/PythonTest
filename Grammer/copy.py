name_list = ["John", "Emma", "Mike", "Sophia", "David"]

# 1.copy()
# list1 = name_list.copy()
# print(list1)

# 2.while
i = 0
while i < len(name_list):
    print(name_list[i], end=" ")
    i += 1

# 3.for
for i in name_list:
    # 遍历序列中的数据
    print(i, end=" ")
