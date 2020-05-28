# 计算0到1000之间偶数的和
result = 0
i = 0
while i <= 1000:
    if i % 2 == 0:
        result += i
    i += 1
print("结果 = %d" % (result))