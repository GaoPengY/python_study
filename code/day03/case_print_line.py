
def print_line():
    """ 打印50个星花 """
    print("*" * 50)

# 打印任意字符组成的分割线
def print_star(star):

    print(star * 50)

print_star("-")

# 打印指定字符，指定数量的分割线
def print_lines(char,count):

    print(char * count)

print_lines("=",30)

# 打印多行分割线
def print_liness(row,chars,counts):
    """
    打印多行分割线
    """
    i = 0
    while i < row:
        print_lines(chars,counts)
        i += 1

print_liness(10,"=",30)