# 变量的格式化输出 %(格式化字符)
# 格式化字符  含义
# %s          字符串
# %d          整数 
# %f          小数
# 两个%         %
a = 10
print("%d 元" % a)
# 有多个变量
b = 10.3
c = 5
d = b * c
print("水果每斤%d元，%f斤总共%f元" % (c,b,d))