# 字典是用来存储 无序 对象的集合
# 列表是 有序 对象的集合

# 字典用{} 定义
# 使用键值对来存储数据
# 键key 是索引
# 值value 是数据
# 键和值用 ： 隔开
# 键必须是唯一的
# 值可以是任意数据类型，键只能使用字符串，数字和元组

xiaming = {"name": "xiaoming",
            "age": 18,
            "gender": True,
            "height": 1.78
}

# 输出顺序和定义顺序无关
print(xiaming)

# 字典的常用操作
# 取值 指定需要取值的key
name = xiaming["name"]
print(name)

# 添加 kay不存在新增
xiaming["like"] = "花朵"
print(xiaming)

# 修改 key存在会修改键值对 
xiaming["name"] = "小明"
print(xiaming)

# 删除
xiaming.pop("like")
print(xiaming)

# 统计键值对的数量
# len函数
len = len(xiaming)
print(len)

# 字典的合并
xiaoer = {"top": "ttt","right": 15,"age": 19}
# 被合并的字典中如果存在当前字典中的key时，会覆盖当前键值对
xiaming.update(xiaoer)
print(xiaming)

# 清空字典
xiaoer.clear()

# 字典的遍历
# key是循环过程中拿到的键
for key in xiaming:
    print("%s : %s" % (key,xiaming[key]))


# 将字典放在列表中遍历
lists = [
    {"name": "xiaoer"},
    {"name": "xiaosan"},
    {"name": "xiaowu"}
]
for name in lists:
    print(name["name"])