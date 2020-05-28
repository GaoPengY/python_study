# 还是买水果案例
price_str = input("请输入价格：")
weight_str = input("请输入重量：")

# 将数据转化为int类，计算单价
total = int(price_str) * int(weight_str)
print(total)

# 案例改进
price = int(input("请输入价格："))
weight = int(input("请输入重量："))
ttl = price * weight