# 1.导入managerSystem模块
from managerSystem import *

# 2.启动系统
# 保证是当前文件运行才启动管理系统
if __name__ == '__main__':
    student_manager = StudentManager()

    student_manager.run()