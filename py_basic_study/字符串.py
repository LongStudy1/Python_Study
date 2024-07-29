name = "\"不止"
print(name)
print("努律"+"努力")
address = "广州市"
print(address+name)
phone = 135
print(address+name, phone)

name = "小龙"
age = 21
# message = "广州市有%s，" % name + "年龄：%s" % age
message = "广州市有%s, 年龄是%s,%d,%f" % (name, age, age, age)
"""
- 和C语言的%d差不多 scanf
"""
print(message)

"""
- m.n控制字符串精度
m控制字符串宽度
.n保留n位小数
"""
num1 = 11.345
print("设置num1宽度位5：num1=%5d" % num1)
print("设置num1宽度为1：num1=%1d" % num1)
print("设置num1精度为2：num1=%.2f" % num1)
print("设置num1宽度为3，精度为1：num1=%3.1f" % num1)

"""
- f"内容{变量}"来快速格式化，不限字符类型，也不限于精度控制
"""
name = "小龙"
age = 18
salary = 100.15
print(f"我是{name}"+f"，年龄{age}"+f"，工资{salary}")

# 表达式格式化
print("1 * 1的结果是%d" % 1*1)
print(f"1 * 1的结果是{1*1}")
print("字符串在Python中是%s类型" % type(name))

# 练习题
