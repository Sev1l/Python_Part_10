## Class Hierarchies
# Task 1 (Laptop computer)

class Computer:
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def get_model(self):
        return self._model

    def get_speed(self):
        return self._speed


class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        super().__init__(model, speed)
        self.weight = weight

    def __str__(self):
        return f'{self.get_model()}, {self.get_speed()} MHz, {self.weight} kg'


laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
