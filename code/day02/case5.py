# 九九乘法表

num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print("%d X %d = %d" % (num1,num2,num1*num2),end = "\t")
        num2 += 1
    print("") 
    num1 += 1

# 转移字符
# \t 在输出文本时保持垂直方向对齐
# \n 换行