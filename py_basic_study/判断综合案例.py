import random
num = random.randint(1, 10)
# print(f"随机产生的数字是：{num}")
if int(input("请输入你猜的数字：")) != num:
    if int(input("猜错了，再猜一次：")) != num:
        if int(input("猜错了，最后再猜一次：")) != num:
            print("Sorry,猜了三次都没中，随机产生的数字是： %s" % num)
        else:
            print("恭喜你，第三次猜对了 %s" % num)
    else:
        print("恭喜你，第二次猜对了 %s" % num)
else:
    print("恭喜你，第一次就猜对了 %s" % num)
