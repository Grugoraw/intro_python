# думаю можно было сделать лучше, учитывая что все предыдущие задания я доробатывал в процессе
# но мозгов и времени уже не хватает
# а еще надеюсь, что правильно понял смысл поставленной задачи
# непонятно только зачем картедж с порядковым номером, что бы сложней доставть было значения? ??
warehouse = []
user_num = int(input("Какое количестов товара вы  хотите ввести: "))
for product_index in range(0, user_num):
    product_name = input("введите наименования товара: ")
    price = float(input("введите цену товара: "))
    quantity = float(input("Введите кол-во товара: "))
    units = input("Введите единицу измерения для товара: ")
    product_lab = {"название": product_name, "цена": price, "количество": quantity, "ед": units}
    warehouse.append((product_index + 1, product_lab))
user_key = input("Введите характеристику для выборки: ")
new_list = []
for element in warehouse:
    new_list.append(element[1].get(user_key))
new_dict = {user_key: new_list}
print(new_dict)