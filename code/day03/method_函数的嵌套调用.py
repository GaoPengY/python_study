# 函数的嵌套调用

def print_str(string):
    """ 打印字符串 """
    print(string)


def get_str():
    """ 获取字符串 """
    return "test"

def test():
    """ 调用函数测试 """
    string = get_str()
    print_str(string)

test()