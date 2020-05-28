# 不同类型变量间的计算
# 数字型变量之间可以直接计算
# bool 在计算时 True= 1，False =0
i = 9
f = 9.1
b = True
print(i + f)
print(i + b)
print(f - b)

# 字符串间的运算: 将两个字符串拼接在一起
first_name = "zhang"
last_name = "san"
print(first_name + last_name)
# 字符串与数字相乘: 重复字符串拼接
print(first_name * 9)
# 除此以外字符串不能进行其他计算

# 变量的输入：获取键盘输入的内容
# 使用input函数
# 用变量接受用户输入的内容
a = input()
print(a)
user = input("请输入用户名称：")
print(user)
# input得到的数据类型都是str
print(type(user))

# 类型转换
# int(x) 将x转为整数
# float(x) 将x转为小数
x = "123"
print(int(x))
print(float(x))