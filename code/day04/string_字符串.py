# 字符串的定义
# 使用"" 或''

str1 = "你好"
# 当定义字符串时需要用到""时，用单引号
str2 = '我的外号是"xiaoer"'
print(str2)

# 从字符串中获取某个字符，使用索引
print(str1[0])

# 字符串的遍历
for c in str2:
    print(c)

# 字符串的常用操作
# len 字符串的长度
print(len(str2))

# count() 方法统计某个小字符串出现的次数
print(str2.count("xi"))

# index() 获取指定小字符串在字符串中的索引
print(str2.index("xi"))

# 判断类型 isXXXXX()方法
# isspace() 判断是只包含空白字符(\t,\r,\n)/空格
space_str = "\t"
res = space_str.isspace()
print(res)

# 判断是否只包含字符串
str1 = "12222"
str2 = "(1)"
# 都不能判断小数
# isdecimal 只能判断数字
print(str1.isdecimal())
# isdigit和isnumericz 可以判断unicode字符
# 如(2) \u002等
print(str1.isdigit())
# isnumeric() 可以判断中文数字
print(str1.isnumeric()

# 查找和替换
# str1 = "nihaoa"
# str1 = "nihaoa"
# startwith 判断字符串是否以某个字符开头


# endwith 判断字符串是否以某个字符开头·


# find 查找 小字符在大字符中出现的索引
# 指定字符串不存在,返回 -1


# replace 替换指定字符


# 大小写转换


# 文本对齐


# 去除空白字符串