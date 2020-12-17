class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        Road.__length = length
        Road.__width = width

    def calc (self, mass_of_asphalt, asphalt_thickness):
        print(f'{Road.__width * Road.__length * mass_of_asphalt * asphalt_thickness / 1000} тонн')



a = Road(20, 5000)
a.calc(25, 5)

