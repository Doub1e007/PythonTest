from my_module2 import *

testA()
# 因为testB不在__all__列表中，所以无法调用
# testB()