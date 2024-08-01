# print("欢迎来到广州动物园")
# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     if int(input("请输入你的VIP级别：")) < 3:
#         print("VIP级别小于3，不可以免费")
#     else:
#         print("恭喜你，VIP级别大于3，可以免费")
# else:
#     print("欢迎小朋友，免费玩")

age = int(input("请输入你的年龄:"))
year = int(input("请输入你的入职年数："))
level = int(input("请输入你的级别"))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("恭喜你，年龄达标了")
        if year > 2:
            print("恭喜你，入职时间和年龄达标了，可以领取礼物")
        elif level > 3:
            print("恭喜你，入职时间和级别都达标了，可以领取礼物")
        else:
            print("很遗憾，虽然你的年龄达标了，但是入职时间和级别都不达标，不可以领取礼物")
    else:
        print("很遗憾，你的年龄太大了，不能领取")
else:
    print("很遗憾，你的年龄太小了，不能领取")

