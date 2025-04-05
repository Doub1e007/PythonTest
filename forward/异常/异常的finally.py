# 需求 尝试以r打开文件 如果有异常以w打开文件 最终关闭文件
try:
    f = open("test1.txt","r")
except Exception as result:
    f = open("test1.txt","w")
else:
    print("没有异常是执行的代码")
finally:
    f.close()