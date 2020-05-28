# python中的算数运算符和变量

# 变量的定义
# 变量名 = 值
a = 10
b = 5

# 基本运算
# 加法
print(a + b)

# 减法
print(a - b)

# 乘法
print(a * b)

# 除法
print(a / b)

# 模余
print(a % b)

# 小案例买东西
# 去商店买5斤香蕉，每斤5元

# 定义价格
price = 5

# 称重
wight = 5
#计算价格
total = price * wight
print(total)

# python中的变量类型
# 案例  小明的个人信息
# 姓名： 小明
# 年龄： 19
# 性别： 男
# 身高： 1.76m
# 体重： 65.3kg
# python在定义变量时不需要指定数据类型
# 运行时解释器根据等号右侧的数据自动推导出，变量中保存的数据类型
# 可以使用type函数查看变量中保存的数据类型
# str 字符串
name = "小明"
print(type(name))
# int 整型
age = 18
print(type(age))
# bool False or True
male = True
print(type(male))
# float 浮点类型
height = 1.76
print(type(height))
weight = 65.3
print(type(weight))

# python中的变量可分为两种：数字型和非数字型
# 数字：
# 整形
# 浮点
# 布尔(非零即真)
# 复数形(complex) 主要用于科学计算

# 非数字
# 字符串
# 列表
# 元组
# 字典

# 扩展: n的x次方的计算
n = 3
x = 5
print(n ** x)