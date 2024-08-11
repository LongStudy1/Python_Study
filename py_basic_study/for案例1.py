text = input("请输入你想判断的字符串有多少个字符a: ")
count = 0
for x in text:
    if x == 'a':
        count += 1
print(f"被统计的字符串有{count}个a")
