# 元组 多个元素组成的序列
# 元组使用() 定义
# 元组变量定义后，不能被修改

# 元组通常用来 保存不同类型的数据

person_info = ("xiaoming",18,1.78)
# 元组中如果只有一个元素，该元素后需要用一个 逗号

# 获取元组中数据的方法和列表相同
print(person_info[0])
print(person_info[1])
print(person_info[2])

# 创建空元组
empty_tuple = ()
# 元组创建后不能修改，因此不建议使用空元组

# 定义只有一个元素的空元组
# 后面的逗号不可省略
one_tuple = (5,)

# 元组的常用操作
# count 获取元素出现的次数
count = person_info.count("xiaoming")
print(count)

# index 获取元素对应的下标
index = person_info.index("xiaoming")
print(index)

# 获取元素个数
print(len(person_info))

# 元组的遍历
for info in person_info:
    print(info)

# 元组的应用
# 作为函数的参数或返回值
# 格式字符串 
# 让列表不可以被修改

# 格式化字符串
print("%s 的年龄是 %d 身高是 %.2f" % person_info)

# 元组和列表的转换
lists = ["xiaoer","xiaosan","xiaosi"]

# 列表转元组
info_tuple = tuple(lists)
print(type(info_tuple))

# 元组转列表
print(type(list(person_info)))

