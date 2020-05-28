# python 中的条件判断，比较运算符，逻辑运算
# 判断语句又称为分支语句
# 判断的定义：满足条件时做某事
# if判断的基本语法
"""
if 条件：
    条件成立执行的代码块
"""
# 输入一个年龄
age = int(input("请输入年龄："))

#判断是否成年
if age >= 18:
    print("成年人！")
print("=============")

# python中的比较运算符
# == 判断是否相等,条件成立返回true
if 1 == 1:
    print("相等")
# != 不等于
print(1 != 2)
# > 大于  >= 大于等于
print( 2 > 1)
# < 小于  <= 小于等于
print( 1 < 2)
print("=============")

# 当条件不成立时，执行的代码
# 使用else关键字
if age >= 18:
    print("成年")
else:
    print("未成年")
print("=============")

# 逻辑运算符
# and 并且
# or  或者
# not 非
# 可以使用逻辑运算符连接多个条件

# and 必须同时满足and连接的多个条件
print(True and False)
print(True and True)
print("=============")
# or 只要一个条件成立
print(True or False)
print(False or False)
print("=============")

# not 取反
print(not True)
print(not False)

# 判断年龄在18到40之间，输出青年
if age >= 18 and age <=40:
    print("青年")

a = int(input())
b = int(input())
# if语句的进阶 elif
if a == b:
    print("======")
elif a > b:
    print(">>>>>>")
else:
    print("<<<<<<")

# if的嵌套
if a > b:
    print("a > b")
    if a == 5:
        print("a = 5")
else:
    print("1111")

