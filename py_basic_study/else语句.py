print("欢迎来到游乐场，儿童免费，成人收费")
age = input("请输入你的年龄：")
if int(age) >= 18:
    print("你已成年，游玩需要买票，10元")
else:
    print("你未成年，不需要买票，请开心玩耍吧~")

"""
-小案例
"""
print("欢迎来到广州动物园")
height = int(input("请输入你的升高（cm）："))
if height > 120:
    print("你的身高超出120CM,需要买票，20元")
else:
    print("你的身高不足120CM,不需要买票，请进~")
