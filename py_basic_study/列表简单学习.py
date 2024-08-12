# 使用[]去定义，或者list()
name_list = ["liang", "yu", "long"]
print(name_list)
print(type(name_list))

name_list.append("596")
name_list.append(True)
print(name_list)
print(type(name_list))

list15= [1, 2, 3]
name_list.append(list15)
print(name_list)
print(type(name_list))

list1 = [1, 2, 3, 4, 5, 6, 7, 8
    , [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(list1[0])
print(list1[8], "*", list1[5])
print(list1[-1], "*", list1[-8])
print(list1[8][-1])


