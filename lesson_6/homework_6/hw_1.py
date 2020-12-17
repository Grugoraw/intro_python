import time
class TrafficLight():
    __color = "Красный"


    def color_red(self):
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "Желтый"

    def color_yellow(self):
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = "Зеленый"

    def color_green(self):
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = "Красный"

    def running(self):
        while True:
            self.color_red()
            self.color_yellow()
            self.color_green()


light = TrafficLight()
light.running()