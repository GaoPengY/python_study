# while循环的基本使用,及赋值运算符
# 打印50次你好
count = 0
while count < 50:
    count += 1
    print("你好")

# 赋值运算符
# =  简单赋值  c = a + b
# += 加法赋值  c += a 等同于 c = c + a
# -= 减法赋值  c -= a 等价于 c = c - a
# 其运算符跟加减法相同

# 循环计算 0-1000 之间数字的和
result = 0
i = 0
while i <= 1000:
    result += i
    i += 1
print("结果 = %d" % (result))
