age = input("请输入你的你的年龄：")
if int(age) < 18:
    print("很抱歉，你还没成年噢！")
if int(age) >= 18:
    print("很高兴，你已经成年了！")

"""
-小案例
"""
print("欢迎来到游乐场，儿童免费，成人收费")
age = input("请输入你的年龄：")
if int(age) >= 18:
    print("你已成年，游玩需要买票，10元")
print("祝你游玩愉快！")
