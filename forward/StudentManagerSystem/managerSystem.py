from student import *
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
        # 1.用户输入姓名、性别、手机号
        name = input('请输入学员姓名：')
        gender = input('请输入学员性别：')
        tel = input('请输入学员手机号：')

        # 2.创建学员对象 -- 类在student文件里 先导入模块 再创建对象
        student = Student(name, gender, tel)

        # 3.将学员对象添加到列表中
        self.student_list.append(student)

        print(self.student_list)
        print(student)

    # 2.3 删除学员
    def del_student(self):
        # 1.用户输入要删除的学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2.遍历列表，如存在则删除 不存在提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                # 删除该学员对象
                self.student_list.remove(i)
                break
        else:
            print('该学员不存在')

        print(self.student_list)

    # 2.4 修改学员信息
    def modify_student(self):
        # 1.用户输入要修改的学员姓名
        modify_name = input('请输入要修改的学员姓名：')

        # 2.遍历列表，如存在则修改 不存在提示学员不存在
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('手机号：')
                print(f'修改该学员信息成功，姓名{i.name}，性别{i.gender}，手机号{i.tel}')
                break
        else:
            print('查无此人')


    # 2.5 查询学员信息
    def search_student(self):
        # 1.用户输入要查询的学员姓名
        search_name = input('请输入要查询的学员姓名：')

        # 2.遍历列表，如存在则显示 不存在提示学员不存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名{i.name}，性别{i.gender}，手机号{i.tel}')
                break
        else:
            print('查无此人')

    # 2.6 显示所有学员信息
    def show_student(self):
        # 打印表头
        print('姓名\t性别\t手机号')

        # 打印学员数据
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 2.7 保存学员信息
    def save_student(self):
        # 1.打开文件
        f = open('student.data', 'w')

        # 2.文件写入 数据
        # 注：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        # [文件对象] 转 [字典]
        new_list = [i.__dict__ for i in self.student_list]

        # 注2：文件内数据要求为字符串类型 需先转换数据类型为字符串再写入数据
        f.write(str(new_list))

        # 3.关闭文件
        f.close()

    # 2.8 加载学员信息
    def load_student(self):
        # 尝试以 r 模式打开数据1文件 文件不存在则读取数据
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 1.读取文件数据
            data = f.read()
            # 2.文件中读取的数据都是字符串且字符串内部为字典数据 故需要转换数据类型再转换字典为对象后存储到学院列表
            # 文件读取出的数据是字符串还原列表类型： [{}] 转换 [学员对象]
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 3.关闭文件
            f.close()