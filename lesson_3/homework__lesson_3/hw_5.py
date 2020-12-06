def sum_list(new_list):
    count = 0
    for element in new_list:
        if element == "q":
            break
        else:
            count = count + int(element)
    return [count, element]

print("Введите числа через пробел, если введете q ввод закончится")
my_number = 0
while True:
    my_list = input("Вввод: ").split()
    my_number = my_number + sum_list(my_list)[0]
    print(my_number)
    if sum_list(my_list)[1] == "q":
        break