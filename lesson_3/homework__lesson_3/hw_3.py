def my_func(a, b, c):
    my_list = [int(a), int(b), int(c)]
    my_list.sort()
    return my_list[1] + my_list[2]

a, b, c = input("Введите число: ").split(" ")
print(my_func(a, b, c))
