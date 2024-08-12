def func1():
    print("---1---")
    func2()
    print("---3---")


def func2():
    print("---2---")


func1()