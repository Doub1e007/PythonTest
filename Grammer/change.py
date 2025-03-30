name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 1.修改指定下标的数据
name_list[0] = "Alicia"
print(name_list)

# 2.逆序 reserve()
list1 = [1,3,2,5,4,6]
list1.reverse()
print(list1)

# 3. sort() 排序 ：升序 默认 reverse = False 和降序 默认升序
list1.sort(reverse=True)
print(list1)