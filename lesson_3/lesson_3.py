"""
Давайте решать интересные задачи!
"""

# def is_cyrilic(data_string, index = -1):
#     last_char = ord(data_string[index])
#     if last_char >= 1072 and last_char <= 1103:
#         print(f"Founded {last_char}")
#         return True
#     else:
#         print("Try more")
#         return False
#
# # input_string = input("Введите строчку: ")
# # flag = is_cyrilic(input_string)
# # print(flag)
#
# def my_max(list_numbers):
#     max_el = 0
#     max_index =0
#     for i in range(len(list_numbers)):
#         if list_numbers[i] >= max_el:
#             max_el = list_numbers[i]
#             max_index = i
#     print(f'Founded index {max_index}, value {max_el}')
#     return max_el, max_index
#
# random_list = [1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 5]
# # result = my_max(random_list)
# # print(f'result {type(result)}')
#
# def print_all(type_of_star, *all_stars):
#     for star in all_stars:
#         print(f'Welcom {type_of_star} {star}!')
#
# input_string = input("Names: ")
# input_string = input_string.split(" ")
# print_all("космонавт", input_string)
#
# numbers = input("Input numbers: ")
# numbers = numbers.split()
#
# print(f'Mapping: ', list(map(int, numbers)))
#
# def mult_5(x):
#     return 5 * x
# print(f' mapping: {list(map(mult_5, random_list))}')

print(f'Lamda : {(lambda x: x*2)(2)}')