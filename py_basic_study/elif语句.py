print("欢迎来到广州动物园")
height = int(input("请输入你的升高（cm）："))
vip_level = int(input("请输入你的VIP级别："))
day = int(input("请告诉我今天几号："))
if height < 120:
    print("你的身高低于120CM,不需要买票，请进~")
elif vip_level > 3:
    print("你的VIP级别大于3，不需要买票，请进~")
elif day == 1:
    print("今天是1号免费日，不需要买票，请进~")
else:
    print("所有条件都不满足,需要买票，20元")

"""
输入写入判断语句中
"""
if int(input("请输入你的升高（cm）：")) < 120:
    print("你的身高低于120CM,不需要买票，请进~")
elif int(input("请输入你的VIP级别：")) > 3:
    print("你的VIP级别大于3，不需要买票，请进~")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，不需要买票，请进~")
else:
    print("所有条件都不满足,需要买票，20元")

"""
-小案例
"""
if int(input("请输入我猜想的数字：")) == 5:
    print("恭喜猜一次就对啦")
elif int(input("猜错了，再猜一次：")) == 5:
    print("恭喜猜两次就对啦")
elif int(input("猜错了，再猜一次：")) == 5:
    print("恭喜猜三次就对啦")
else:
    print("Sorry，猜了三次都不对！我猜的数字是5")

