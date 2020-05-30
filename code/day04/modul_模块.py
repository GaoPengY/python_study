# 每一个python文件都是一个模块

# 使用import 导入
# 模块中定义的全局变量和函数都可直接被外界使用

# 导入随机数模块 random
import random

# 生成1到10之间的随机数
r = random.randint(1,10)

print(r)

# pyc是已经被编译过的文件
# 直接使用pyc文件可以提高执行效率