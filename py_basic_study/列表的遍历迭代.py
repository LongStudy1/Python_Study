my_list = [1, 2, 3, 4, 5]
length = 0
while length < len(my_list):
    print(f"{my_list[length]}\t", end='')
    length += 1

print()

for i in my_list:
    print(f"{i}\t", end='')


