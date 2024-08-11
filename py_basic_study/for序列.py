# range(num)
# 获取[0,***,num-1]
# range(num1, num2)
# 获取[num1, num2-1]
# range(num1, num2, step)
# 获取[num1, num1+step,***,max(num2-1)]
for x in range(10):
    print(x)
for x in range(0, 5):
    print(x, end='')
print()
for x in range(0, 9, 3):
    print(f"{x} ", end=' ')
