user_month = int(input("Введите число месяца от 1 до 12: "))
# Первая попытка
season = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
print(season[user_month - 1])
# Вторая попытка
season_dic = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
              10: "Осень", 11: "Осень", 12: "Зима"}
print(season_dic.get(user_month))
# не все дается сразу, решения пришло во премя попыток решить 6 задание
season_dic2 = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
for key in season_dic2.keys():
    for value in season_dic2.get(key):
        if user_month == value:
            print(key)
            break