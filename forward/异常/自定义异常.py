# 1.自定义异常类 继承Exception
class ShortInputError(Exception):
    def __init__(self,length,min_length):
        # 用户输入的密码长度
        self.length = length
        # 密码的最小长度
        self.min_length = min_length

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length},长度至少为{self.min_length}'

# 2.抛出异常 尝试执行用户输入密码，如果密码小于3 抛出异常
def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(con),3)
# 3.捕获异常
    except Exception as result:
        print(result)
    else:
        print('密码输入正确')
main()