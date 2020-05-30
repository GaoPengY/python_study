# 列表是python中使用最频繁的数据类型
# 列表是专门用来存储一串信息的
# 列表用[]定义，数据之间用","隔开

name_list = ["xiaoer","xiaosan","xiaosi"]

print(name_list)

# 从列表中获取指定数据
# 列表中每个元素都有一个对应的下标，从0开始
# 通过下标可以获取对应的值
print(name_list[0])
print(name_list[1])
print(name_list[2])

# 列表的常用操作
# 获取指定数据的下标(索引)
print(name_list.index("xiaosan"))

# 修改列表中指定位置的元素
name_list[2] = "小四"

# 添加元素的方法
# 追加到列表的末尾
name_list.append("xiaowu")
print(name_list)
# 插入元素到指定索引
name_list.insert(1,"小三")
print(name_list)
# 扩展 将另一个列表扩展到当前列表的末尾
names = ["xiaoxiao","xiaoqi"]
name_list.extend(names)
print(name_list)

# 删除元素
# clear  清空列表
names.clear()
print(names)

# remove() 删除指定元素
name_list.remove("xiaoxiao")
print(name_list)

# pop() 删除任意元素不指定，默认删除最后的元素
# 删除最后的元素
name_list.pop()
print(name_list)
# 删除索引为2的元素
name_list.pop(2)
print(name_list)

# del 关键字 ，也可以用来删除列表元素
# 删除索引为1的元素，
# del 关键字的本质是将变量从内存中删除
# del 关键字慎用，建议使用列表提供的方法
del name_list[1]

# 统计列表变量元素个数的方法
# len函数 获取列表长度
name_len = len(name_list)
print(name_len)

# count() 方法用来统计某个元素再列表中出现的次数
count = name_list.count("xiaoer")
print(count)

# remove() 方法会删除第一次出现在列表中的数据

# 排序
# sort() 默认升序
name_list.sort()
print(name_list)
# sort(reversed = True) 降序
name_list.sort(reverse = True)
print(name_list)

# reverse 反转
name_list.reverse()
print(name_list)

# 关键字，函数，方法区别
# 关键字是 python 内置的，具有特殊意义的标识符
# 获取python 关键字列表 keyword.kwlist
import keyword
print(keyword.kwlist)
# python 中一共有35个关键字
print(len(keyword.kwlist))

# 函数 封装了独立功能，可以直接使用
# 函数只能死记硬背

# 方法名可以被只能提示