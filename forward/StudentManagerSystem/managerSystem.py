class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一、程序入口函数
    def run(self):
        # 1. 加载文件存储的数据
        self.load_student()
        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3. 用户选择功能
            menu_num = int(input('请输入您需要的功能序号：'))

            # 4. 根据用户输入的序号执行不同的功能 -- 通过用户执行1 执行1添加
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break


    # 二、系统功能函数
    # 2.1 显示功能菜单 --打印序号的功能对应关系 静态方法
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1. 添加学员')
        print('2. 删除学员')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 保存学员信息')
        print('7. 退出系统')

    # 2.2 添加学员
    def add_student(self):
        print('添加学员')

    # 2.3 删除学员
    def del_student(self):
        print('删除学员')

    # 2.4 修改学员信息
    def modify_student(self):
        print('修改学员信息')

    # 2.5 查询学员信息
    def search_student(self):
        print('查询学员信息')

    # 2.6 显示所有学员信息
    def show_student(self):
        print('显示所有学员信息')

    # 2.7 保存学员信息
    def save_student(self):
        print('保存学员信息')

    # 2.8 加载学员信息
    def load_student(self):
        print('加载学员信息')