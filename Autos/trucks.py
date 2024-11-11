from Autos.cars import Car

class Big(Car):

    def __init__(self, model, year, engine_size, price, mileage):
        super().__init__(model, year, engine_size, price, mileage)
        self.wheels = "8"


    def description(self):
        description = (f"Модель - {self.model}, год выпуска - {self.year}, объём двигателя - {self.engine_size}, "
                  f"цена - {self.price}, пробег - {self.mileage}, количество колёс - {self.wheels}")
        return description