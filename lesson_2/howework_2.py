user_list = list(input("Введите свой список: "))
if len(user_list) % 2 == 0:
    for i in range(0, len(user_list), 2):
        user_list[i], user_list[i+1] = user_list[i+1],user_list[i]
else:
    for i in range(0, len(user_list)-1, 2):
        user_list[i], user_list[i+1] = user_list[i+1],user_list[i]
print(user_list)