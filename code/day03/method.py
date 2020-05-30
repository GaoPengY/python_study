# 函数
# 具有独立功能的代码块
# 函数的定义：
"""
def 函数名():
    代码块
"""

def multiplication_table():
    num1 = 1
    while num1 <= 9:
        num2 = 1
        while num2 <= num1:
            print("%d X %d = %d" % (num1,num2,num1*num2),end = "\t")
            num2 += 1
        print("") 
        num1 += 1

def print_hello():
    print("hello")
    print("hello")

# 函数的调用
print_hello()

name = "小明"


def print_name(name):
    """ 输出姓名 """
    print(name)

print_name(name)

def sum(num1,num2):
    """" 计算两数之和 """
    return num1 + num2
# return 的注意事项
# return 之后的代码不会再继续 执行

res = sum(10,20)
print(res)

