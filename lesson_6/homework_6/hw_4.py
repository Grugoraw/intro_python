class Car():

    def __init__(self, name, color, speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина поехала")
        self.speed = 100

    def stop(self):
        print("Машина отсановилась")
        self.speed = 0

    def turn(self, direction):
        if self.speed == 0:
            print('Машна стоит, и не может поварачивать')
        else:
            print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы привышаете скоростной режим, сбросте скорость')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы привышаете скоростной режим, сбросте скорость')


class PoliceCar(Car):
    pass


car_1 = WorkCar("Порущик", "Черный")
car_1.go()
car_1.show_speed()
car_1.turn('лево')
car_1.stop()
car_1.show_speed()

car_2 = SportCar("BMW", "Красный", 250)
car_2.go()
car_2.show_speed()

car_3 = TownCar("KIA", "белый")
car_3.go()
car_3.show_speed()

car_4 = PoliceCar("Skoda", "Синий", 55, True)
car_4.go()
car_4.show_speed()