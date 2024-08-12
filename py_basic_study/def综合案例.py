money = 5000000
name = input("请输入你的姓名: ")


def query():
    # print("----------查询余额----------")
    print(f"{name}你好，你的余额有：{money}元")


def saving(num):
    global money
    money += num
    print("----------存款----------")
    print(f"{name}你好，存款成功，您目前的余额有：{money}元")


def taking(num):
    global money
    money -= num
    print("----------取款----------")
    print(f"{name}你好，取款成功，您目前的余额有：{money}元")


def main():
    print("----------主菜单----------")
    print(f"{name}你好，欢迎来到龙龙银行，请按提示操作：")
    print("1.查询余额   [请输入1]")
    print("2.存款\t   [请输入2]")
    print("3.取款\t   [请输入3]")
    print("4.退出\t   [请输入4]")
    return input("请输入你的选择：")


while True:
    key = main()
    if key == "1":
        query()
    elif key == "2":
        num1 = int(input("请输入你的存款金额："))
        saving(num1)
    elif key == "3":
        num2 = int(input("请输入你的取款金额："))
        taking(num2)
    else:
        print("程序退出啦！")
        break
