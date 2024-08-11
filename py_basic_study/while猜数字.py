import random

num = random.randint(1, 100)
flag = True
counter = 0
# print("随机数是：%d" % num)
while flag:
    cai = int(input("请输入你的数字："))
    counter += 1
    if cai > num:
        print("猜大了")
    elif cai < num:
        print("猜小了")
    else:
        flag = False
print("恭喜你猜对了，总共猜了%d次" % counter)
