# 模拟火车站安检
# 有车票
has_ticket = True
# 不安全
unsafe = True

# 检查是否有票
if has_ticket:
    print("请进站")
    # 检查是否携带不安全物品
    if unsafe:
        print("携带了禁止物，不允许进站")
    else:
        print("检查通过")
else:
    print("请购买查票后进站")
