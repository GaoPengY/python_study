# 石头剪刀布小游戏
# import关键字导入 工具包
# 玩家输入1，2，3分别代表石头，剪刀，布
# 电脑随机出拳
# 引入随机数工具包
import random
# 玩家出拳
palyer = int(input("请输入(石头1/剪刀2/布3)"))

# 电脑出拳
# randint(a,b) 随机返回[a,b]集合之间的整数，a < b
computer = random.randint(1,3)

print("玩家出拳 %d - 电脑出拳%d" % (palyer,computer))

# 比较
if ((palyer == 1 and computer == 2) or 
    (palyer == 2 and computer == 3) or 
    (palyer == 3 and computer == 1)):
    print("恭喜你赢了")
elif palyer == computer:
    print("平局")
else:
    print("你输了")

