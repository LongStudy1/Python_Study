"""
print("请告诉我你是谁：")
name = input()
"""
# 输入字符串类型
name = input("请告诉我你是谁：")
print("Get！你是：%s" % name)
# 输入数字类型
num = input("你的钱包余额：")
print("钱包余额类型是：", type(num))
# 转换为float类型
num = float(num)
print("输入是字符串类型，强转为：", type(num))
