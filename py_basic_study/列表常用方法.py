name_list = ["liang", "yu", "long", "吗"]
# print(name_list)
# print(type(name_list))

name_list.append("597")
name_list.append(False)
# print(name_list)
# print(type(name_list))

list15 = [1, 2, 3, 4, 5]
name_list.append(list15)
# print(name_list)
# print(type(name_list))

print(f'"yu"在list中的下标是{name_list.index("yu")}')
print(name_list)
name_list[4] = "不是"
print(f"修改[4]后的name_list:{name_list}")

name_list.insert(1, "不知道")
print(name_list)

# append是追加
name_list.append([9, 8, 7])
print(name_list)

# 追加单个元素
name_list.extend([1, 2, [3, 4]])
print(name_list)

# 删除指定下标
del name_list[4]
print(name_list)

str1 = name_list.pop(1)
print(str1)
name_list.insert(3, "yu")
print(name_list)
name_list.remove("yu")
print(name_list)

name_list.insert(1, "yu")
count = name_list.count("yu")
print(name_list)
print(count)

length = len(name_list)
print(length)

name_list.clear()
print(name_list)
