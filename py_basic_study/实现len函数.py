str1 = "liang"
str2 = "yu"
str3 = "long"


# count_str1 = 0
# for i in str1:
#     count_str1 += 1
# print(f"字符{str1}的长度是{count_str1}")
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)

