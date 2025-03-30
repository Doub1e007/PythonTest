class Washer():
    def __init__(self):
        self.width = 500

    def __del__(self):
        print('对象被删除了')

haier = Washer()