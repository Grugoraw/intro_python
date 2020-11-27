# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
#1 вариант
user_text = input("Введите текст: ")
new_str = ""
count = 0
count_str = 1
for i in user_text:
    if not i == " ":
        new_str = new_str + i
        count = count + 1
        if count > 9:
            print(f"{count_str}. {new_str}")
            count = 0
            count_str = count_str + 1
            new_str = ""
    else:
        print(f"{count_str}. {new_str}")
        new_str = ""
        count = 0
        count_str = count_str + 1
print(f"{count_str}. {new_str}")

#2 вариант
new_list = user_text.split()
count_str = 1
for element in new_list:
    if len(element) < 10:
        print(f"{count_str}. {element}")
        count_str = count_str + 1
    else:
        count = 0
        new_str = ""
        for i in element:
            if count < 10:
                new_str = new_str + i
                count = count + 1
            else:
                print(f"{count_str}. {new_str}")
                new_str = i
                count = 0
                count_str = count_str + 1
        print(f"{count_str}. {new_str}")

