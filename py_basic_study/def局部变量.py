num = 100


def test_a():
    # num = 100
    print(num)


def test_b():
    # 无法修改全局变量num的值，相当于定义新变量
    num = 200
    print(num)


def test_c():
    # 加上global表示这个是全局变量
    global num
    num = 300
    print(num)


test_a()
test_b()
test_c()
print(num)

