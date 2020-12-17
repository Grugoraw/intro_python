class Worker():
    name = ""
    surname = ""
    position = ""
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {"wage": wage, "bonus": bonus}
        print(Worker._income)

    def income(self):
        return Worker._income['wage'] + Worker._income['bonus']


class Position(Worker):

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_incom(self):
        print(f'{self._income["wage"] + self._income["bonus"]} рублей')


a = Position("Иван", "Иванов", "Бухгалтер", 20000, 5000)
a.get_full_name()
a.get_total_incom()

