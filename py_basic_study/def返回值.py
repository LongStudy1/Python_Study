def add(a, b):
    """
    函数说明
    :param a: 相加的其中1个数字
    :param b: 相加的另一个数字
    :return: 返回a+b的相加值
    """
    return a + b


result = add(1, 587)
print(result)


def say_hi():
    print('hi')


def say_hello():
    print('hello')
    return 'hello'


result1 = type(say_hi())
result2 = type(say_hello())
print(f"无返回值的def函数返回内容类型为：{result1}")
print(f"有返回值的def函数返回内容类型为：{result2}")


def check_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None


result = check_age(18)
if not result:
    print("未成年，不可以进入网吧")
