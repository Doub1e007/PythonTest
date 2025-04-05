# 需求1：尝试只读打开test.txt文件 文件存在读取内容 不存在提示用户
# 需求2：读取内容：循环次数，当无内容的时候退出循环，意外终止是提示用户
import time
try:
    f = open('test.txt')
    # 尝试循环读取内容
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果读取文件过程中产生了异常 就会被捕获到
        # 测试 ctrl + c
        print('程序被意外终止')
    finally:
        f.close()
        print('关闭文件')
except:
    print('fail to open file')