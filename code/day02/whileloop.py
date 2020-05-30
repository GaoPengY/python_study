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

# break 和 continue
# break 终止循环
a = 0
while a < 10:
    a += 1
    print(a)
    if a == 5:
        break

# continue 跳过当前循环
b = 0
while b < 10:
    b += 1
    if b == 5:
        continue
    print(b)

# 循环嵌套
k = 0
while k < 5:
    k += 1
    print("*" * k)
# 使用循环嵌套

j = 0
while j < 5:
   
    h = 0
    while h <= j:
        h += 1
        # print函数默认会换行
        # 不希望换行print("", end = "")
        print("*",end = "")
    # 每行结束后换行
    print("")
    j += 1
        
            
            
        