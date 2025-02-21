name_list = ['TOM','Lily','ROSE']

# 需求 注册邮箱 用户输入一个账号名，判断这个账号是否存在 如果存在 提示用户 否则提示可以注册
'''
1. 用户输入账号
2. 判断账if...else
'''
name = input('请输入您的账号：')

if name in name_list:
    # 提示用户名已经存在
    print(f'您输入的用户名是{name}，该账号已存在，请重新输入')
else:
    # 提示用户可以注册
    print(f'您输入的名字是{name},该账号可以注册')