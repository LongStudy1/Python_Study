import random

salary = 10000
while salary > 0:
    for x in range(1, 20):
        sui = random.randint(1, 10)
        if sui < 5:
            print(f"第{x}个员工绩效分{sui},不足5分，不予发工资")
            continue
        if salary >= 1000:
            salary -= 1000
            print(f"给第{x}个员工发放1000工资，公司账户余额:{salary}元")
        else:
            print("工资发完了 ，没有了")
            break

