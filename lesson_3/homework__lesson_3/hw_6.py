def int_func(user_string):
    user_string = user_string.capitalize()
    return user_string

def all_up(user_string):
    string_list = user_string.split(' ')
    new_string = "".join(int_func(el) + " " for el in string_list)
    return new_string


user_string = input("input text: ")
print(all_up(user_string))
