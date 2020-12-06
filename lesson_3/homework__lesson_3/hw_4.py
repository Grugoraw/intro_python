'''
простой метод
def my_func(x,y):
    return x ** y
'''

def my_func(x,y):
    number = x
    for i in range(1, y):
        number = number * x
    return number
x = int(input("enter x "))
y = int(input("enter y "))
print(my_func(x, y))