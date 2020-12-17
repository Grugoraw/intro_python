top_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
user_num = int(input("Ввведите число: "))

if user_num <= top_list[len(top_list)-1]:
    top_list.append(user_num)
else:
    for index in range(0, len(top_list)):
        if user_num > top_list[index]:
            top_list.insert(index, user_num)
            break

print(top_list)